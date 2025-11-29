"""Observability manager for tracking system interactions."""
import logging
from datetime import datetime
from typing import Dict, Any, List


class ObservabilityManager:
    """Manages observability and logging of system interactions."""
    
    def __init__(self):
        self.interactions: List[Dict[str, Any]] = []

    def log(self, query: str, agent_responses: Dict[str, str], final_response: str):
        """Log an interaction with all agent responses."""
        rec = {
            "time": datetime.now().isoformat(),
            "query": query,
            "agent_responses": {k: v[:400] for k, v in agent_responses.items()},
            "final_response": final_response[:800]
        }
        self.interactions.append(rec)
        logging.info("Observability log appended: query=%s", query)

    def report(self) -> Dict[str, Any]:
        """Generate a report of recent interactions."""
        return {
            "total_interactions": len(self.interactions),
            "recent": self.interactions[-10:] if self.interactions else []
        }

    def get_agent_usage_stats(self) -> Dict[str, int]:
        """Get statistics on agent usage."""
        stats = {}
        for interaction in self.interactions:
            for agent in interaction["agent_responses"].keys():
                stats[agent] = stats.get(agent, 0) + 1
        return stats