"""Base agent class for all specialized agents."""
import logging
from datetime import datetime
from typing import Dict, Any, List
import google.generativeai as genai

from src.utils.helpers import safe_generate, MODEL_ID, GEN_CONFIG


class BaseAgent:
    """Base class for all specialized agents."""
    
    def __init__(self, name: str, system_prompt: str, model_id: str = MODEL_ID):
        self.name = name
        self.system_prompt = system_prompt
        try:
            self.model = genai.GenerativeModel(model_id, generation_config=GEN_CONFIG)
        except TypeError:
            self.model = genai.GenerativeModel(model_id)
        self.history: List[Dict[str, Any]] = []

    def build_prompt(self, user_prompt: str, context: str = "") -> str:
        """Build the prompt for the agent."""
        return f"""SYSTEM:
{self.system_prompt}

CONTEXT:
{context}

USER:
{user_prompt}

Provide a concise helpful response."""

    def generate_response(self, user_prompt: str, context: str = "") -> str:
        """Generate a response from the agent."""
        prompt = self.build_prompt(user_prompt, context)
        logging.info("[%s] generate called. prompt_len=%d", self.name, len(prompt))
        result = safe_generate(self.model, prompt)
        self.log_interaction(user_prompt, result)
        return result

    def log_interaction(self, prompt: str, response: str):
        """Log the interaction for observability."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "prompt": prompt,
            "response_summary": response[:400]
        }
        self.history.append(entry)
        logging.info("Interaction logged for %s", self.name)