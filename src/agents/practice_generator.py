"""Practice Generator Agent for creating exercises."""
from .base_agent import BaseAgent


class PracticeGeneratorAgent(BaseAgent):
    """Agent for generating progressive programming exercises."""
    
    def __init__(self):
        prompt = """You are PracticeGenerator: provide short progressive exercises (easy, medium, hard) for the concept requested, with example input/output or tests."""
        super().__init__("PracticeGenerator", prompt)