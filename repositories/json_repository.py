import json
import os
from typing import List, Optional
from repositories.base import BaseRepository
from models.user import User
from models.book import Book

class JSONRepository(BaseRepository):
    def __init__(self, file_path: str = "data/storage.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            self._save_data({"users": [], "books": [], "categories": [], "ratings": [], "history": []})

    def _load_data(self) -> dict:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _save_data(self, data: dict) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def save_user(self, user: User) -> None:
        data = self._load_data()
        for i, existing in enumerate(data["users"]):
            if existing["id"] == user.id:
                data["users"][i] = user.to_dict()
                self._save_data(data)
                return
        data["users"].append(user.to_dict())
        self._save_data(data)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        for u in self._load_data()["users"]:
            if u["id"] == user_id: return User.from_dict(u)
        return None

    def get_all_users(self) -> List[User]:
        return [User.from_dict(u) for u in self._load_data()["users"]]

    def save_book(self, book: Book) -> None:
        data = self._load_data()
        for i, existing in enumerate(data["books"]):
            if existing["id"] == book.id:
                data["books"][i] = book.to_dict()
                self._save_data(data)
                return
        data["books"].append(book.to_dict())
        self._save_data(data)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        for b in self._load_data()["books"]:
            if b["id"] == book_id: return Book.from_dict(b)
        return None

    def get_all_books(self) -> List[Book]:
        return [Book.from_dict(b) for b in self._load_data()["books"]]