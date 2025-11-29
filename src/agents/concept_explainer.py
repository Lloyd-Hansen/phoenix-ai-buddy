"""Concept Explainer Agent for explaining programming concepts."""
from .base_agent import BaseAgent


class ConceptExplainerAgent(BaseAgent):
    """Agent for explaining programming concepts clearly."""
    
    def __init__(self):
        prompt = """You are ConceptExplainer: explain programming concepts clearly using simple definitions, a short example, and a real-world analogy."""
        super().__init__("ConceptExplainer", prompt)