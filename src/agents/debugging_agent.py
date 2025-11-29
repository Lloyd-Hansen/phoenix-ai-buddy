"""Debugging Agent for identifying and fixing runtime errors."""
from .base_agent import BaseAgent


class DebuggingAgent(BaseAgent):
    """Agent for identifying root causes of runtime errors."""
    
    def __init__(self):
        prompt = """You are DebuggingAgent: identify root causes of runtime errors and provide minimal reproducible fixes plus explanation."""
        super().__init__("DebuggingAgent", prompt)