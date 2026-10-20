# models/category.py

from typing import Dict, Any

class Category:
    def __init__(self, category_id: int, name: str):
        self.id = category_id
        self.name = name.strip()

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Category":
        return cls(category_id=data["id"], name=data["name"])