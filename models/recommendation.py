# models/recommendation.py

from typing import Dict, Any

class Recommendation:
    def __init__(self, user_id: int, book_id: int, reason: str, score: float):
        self.user_id = user_id
        self.book_id = book_id
        self.reason = reason
        self.score = score

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "reason": self.reason,
            "score": self.score
        }