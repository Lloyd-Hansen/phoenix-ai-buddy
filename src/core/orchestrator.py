"""Orchestrator agent for routing queries to specialized agents."""
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

from src.agents.base_agent import BaseAgent
from src.core.session_manager import SessionManager
from src.core.observability import ObservabilityManager


class OrchestratorAgent(BaseAgent):
    """Orchestrator that routes queries to appropriate specialized agents."""
    
    def __init__(self, session_manager: SessionManager, observability: ObservabilityManager):
        prompt = """You are OrchestratorAgent: route user queries to specialized agents, gather their outputs, and synthesize a concise unified answer. You can also handle general conversation as a helpful AI assistant."""
        super().__init__("OrchestratorAgent", prompt)
        self.session_manager = session_manager
        self.observability = observability
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, name: str, agent: BaseAgent):
        """Register a specialized agent."""
        self.agents[name] = agent
        logging.info("Registered agent: %s", name)

    def decide_agents(self, user_query: str, has_code: bool = False) -> List[str]:
        """Decide which agents should handle the query."""
        q = user_query.lower().strip()
        selected: List[str] = []

        # General chat and casual conversation - check this FIRST
        general_chat_patterns = [
            "hello", "hi", "hey", "how are you", "what's up", "whats up",
            "good morning", "good evening", "good night", "good afternoon",
            "who are you", "what can you do", "how's it going", "hows it going",
            "tell me a joke", "how do you feel", "what do you think about",
            "thanks", "thank you", "appreciate it", "bye", "goodbye", "see you",
            "how old are you", "where are you from", "what's your name", "whats your name",
            "nice to meet you", "pleasure to meet you", "how have you been",
            "what's new", "whats new", "how's your day", "hows your day"
        ]
        
        # Check if the query is primarily general chat
        is_general_chat = any(pattern in q for pattern in general_chat_patterns)
        
        # For very short messages, prioritize general chat
        if len(q.split()) <= 3 and any(word in q for word in ["hi", "hello", "hey", "bye", "thanks"]):
            is_general_chat = True

        if is_general_chat:
            selected.append("GeneralChatAgent")
            # For pure general chat, don't add other agents
            return selected

        # Programming-specific queries (only if not general chat)
        if any(word in q for word in ["explain", "what is", "why", "how does", "define", "meaning of", "tell me about"]):
            selected.append("ConceptExplainer")

        if has_code or any(word in q for word in ["review", "optimize", "refactor", "improve code", "code quality", "check my code"]):
            selected.append("CodeReviewer")

        if any(word in q for word in ["error", "bug", "traceback", "exception", "fix", "not working", "broken", "debug"]):
            selected.append("DebuggingAgent")

        if any(word in q for word in ["exercise", "practice", "problem", "quiz", "challenge", "task", "question"]):
            selected.append("PracticeGenerator")

        if any(word in q for word in ["generate", "create", "write", "full program", "complete code", "code snippet", "make a", "give me"]):
            selected.append("CodeGenerator")

        # If no specific agent selected, use ConceptExplainer as default for programming questions
        if not selected and len(q.split()) > 2:  # More than 2 words suggests substantive query
            selected.append("ConceptExplainer")
        elif not selected:
            # Very short, ambiguous queries go to GeneralChat
            selected.append("GeneralChatAgent")

        logging.info("Decide agents for query: '%s' -> %s", user_query, selected)
        return selected

    def process_query(self, user_query: str, user_code: str = "") -> Dict[str, Any]:
        """Process a user query by routing to appropriate agents."""
        ctx = json.dumps(self.session_manager.get_context(), indent=2)
        has_code = bool(user_code and user_code.strip())
        agent_names = self.decide_agents(user_query, has_code=has_code)
        responses: Dict[str, str] = {}

        # Get responses from each selected agent
        for name in agent_names:
            agent = self.agents.get(name)
            if not agent:
                responses[name] = f"[{name} not registered]"
                continue

            if name in ["CodeReviewer", "DebuggingAgent"] and has_code:
                prompt_for_agent = f"User Query: {user_query}\n\nCode to analyze:\n{user_code}"
            else:
                prompt_for_agent = user_query

            try:
                res = agent.generate_response(prompt_for_agent, ctx)
            except Exception as e:
                logging.error("Agent %s error: %s", name, str(e))
                res = f"[{name} ERROR] {str(e)}"
            responses[name] = res

        # Synthesize final response
        if len(agent_names) == 1:
            final = list(responses.values())[0]
        else:
            integration_prompt = f"""
            USER QUERY:
            {user_query}

            {'USER CODE:' + user_code if has_code else 'NO CODE PROVIDED'}

            SESSION CONTEXT:
            {ctx}

            SPECIALIZED AGENT RESPONSES:
            {json.dumps(responses, indent=2)}

            Please synthesize these responses into a coherent, helpful final answer.
            Start by listing which specialized agents were consulted, then provide an integrated answer.
            """
            final = self.generate_response(integration_prompt, ctx)

        self._update_session_from_responses(responses, user_query)
        self.observability.log(user_query, responses, final)

        return {
            "final_response": final,
            "agent_responses": responses,
            "agents_consulted": agent_names
        }

    def _update_session_from_responses(self, responses: Dict[str, str], user_query: str):
        """Update session based on agent responses."""
        # Only update session for programming-related interactions
        if "GeneralChatAgent" in responses and len(responses) == 1:
            return  # Skip session updates for pure general chat

        join_text = " ".join(responses.values()).lower()
        user_query_lower = user_query.lower()

        concepts = [
            "function", "loop", "class", "list", "dictionary", "recursion",
            "generator", "decorator", "context manager", "exception", "module",
            "inheritance", "polymorphism", "encapsulation", "abstraction"
        ]

        for concept in concepts:
            if (concept in join_text or concept in user_query_lower) and \
               concept not in self.session_manager.get_context().get("concepts_covered", []):
                self.session_manager.append_concept(concept)
                self.session_manager.add_progress(5)

        if "PracticeGenerator" in responses:
            self.session_manager.add_exercise(user_query)

        if "CodeReviewer" in responses or "DebuggingAgent" in responses:
            self.session_manager.add_code_review({
                "query": user_query,
                "timestamp": datetime.now().isoformat()
            })