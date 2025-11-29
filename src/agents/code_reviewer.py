"""Code Reviewer Agent for analyzing and improving code."""
from .base_agent import BaseAgent


class CodeReviewerAgent(BaseAgent):
    """Agent for analyzing code for bugs, readability, and efficiency."""
    
    def __init__(self):
        prompt = """You are CodeReviewer: analyze provided code for bugs, readability, and efficiency. Provide fixed code or suggestions and short justification."""
        super().__init__("CodeReviewer", prompt)