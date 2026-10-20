# models/user.py

from typing import Dict, Any
from utils.validators import Validator

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name.strip()
        self._email = None
        self.email = email  # تمرير الإيميل عبر الـ Setter للتحقق منه

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = Validator.validate_email(value)

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(user_id=data["id"], name=data["name"], email=data["email"])