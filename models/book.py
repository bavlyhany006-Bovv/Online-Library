# models/book.py

from typing import Dict, Any
from utils.validators import Validator

class Book:
    def __init__(self, book_id: int, title: str, author: str, category_id: int, available_copies: int):
        self.id = book_id
        self.title = title.strip()
        self.author = author.strip()
        self.category_id = category_id
        self._available_copies = 0
        self.available_copies = available_copies  # حماية عدد النسخ المتاحة

    @property
    def available_copies(self) -> int:
        return self._available_copies

    @available_copies.setter
    def available_copies(self, value: int):
        self._available_copies = Validator.validate_non_negative_int(value, "available_copies")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "category_id": self.category_id,
            "available_copies": self.available_copies
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            category_id=data["category_id"],
            available_copies=data["available_copies"]
        )