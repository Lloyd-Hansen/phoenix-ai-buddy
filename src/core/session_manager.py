"""Session management for tracking user progress."""
import logging
from datetime import datetime
from typing import Dict, Any


class SessionManager:
    """Manages user sessions and progress tracking."""
    
    def __init__(self):
        self.context: Dict[str, Any] = {}

    def create_session(self, user_id: str, skill_level: str = "beginner"):
        """Create a new user session."""
        session_id = f"session_{user_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.context = {
            "session_id": session_id,
            "user_id": user_id,
            "skill_level": skill_level,
            "concepts_covered": [],
            "progress_score": 0,
            "exercises_completed": [],
            "code_reviews": [],
            "created_at": datetime.now().isoformat()
        }
        logging.info("Created session %s for user %s", session_id, user_id)
        return session_id

    def get_context(self) -> Dict[str, Any]:
        """Get the current session context."""
        return self.context

    def append_concept(self, concept: str):
        """Add a concept to the covered concepts list."""
        if concept not in self.context["concepts_covered"]:
            self.context["concepts_covered"].append(concept)

    def add_progress(self, amount: int = 5):
        """Add progress points to the session."""
        self.context["progress_score"] += amount

    def add_exercise(self, exercise: str):
        """Add a completed exercise to the session."""
        self.context["exercises_completed"].append(exercise)

    def add_code_review(self, review: Dict[str, str]):
        """Add a code review to the session."""
        self.context["code_reviews"].append(review)