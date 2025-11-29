"""Code Generator Agent for creating complete programs."""
from .base_agent import BaseAgent


class CodeGeneratorAgent(BaseAgent):
    """Agent for generating complete runnable code."""
    
    def __init__(self):
        prompt = """You are CodeGenerator: generate complete runnable code with comments. Provide full programs or scripts based on the user's request."""
        super().__init__("CodeGenerator", prompt)