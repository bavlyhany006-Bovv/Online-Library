# models/rating.py

from typing import Dict, Any, Optional
from utils.validators import Validator

class Rating:
    def __init__(self, rating_id: int, user_id: int, book_id: int, score: float, review: Optional[str] = ""):
        self.id = rating_id
        self.user_id = user_id
        self.book_id = book_id
        self._score = 0.0
        self.score = score  # يمر عبر الـ Setter للحماية (1 إلى 10)
        self.review = review.strip() if review else ""

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, value: float):
        self._score = Validator.validate_rating_score(value)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "score": self.score,
            "review": self.review
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Rating":
        return cls(
            rating_id=data["id"],
            user_id=data["user_id"],
            book_id=data["book_id"],
            score=data["score"],
            review=data.get("review", "")
        )