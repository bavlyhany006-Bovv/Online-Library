 # models/history.py

from enum import Enum
from datetime import datetime
from typing import Dict, Any

class ReadingStatus(str, Enum):
    """حالات استعارة وقراءة الكتاب."""
    BORROWED = "borrowed"
    READING = "reading"
    COMPLETED = "completed"


class ReadingHistory:
    def __init__(self, user_id: int, book_id: int, status: ReadingStatus, date: datetime = None):
        self.user_id = user_id
        self.book_id = book_id
        self.status = status if isinstance(status, ReadingStatus) else ReadingStatus(status)
        self.date = date or datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """تحويل البيانات إلى Dict لسهولة الحفظ في JSON."""
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "status": self.status.value,
            "date": self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ReadingHistory":
        """إنشاء أوبجيكت من Dict عند القراءة من JSON."""
        return cls(
            user_id=data["user_id"],
            book_id=data["book_id"],
            status=ReadingStatus(data["status"]),
            date=datetime.fromisoformat(data["date"])
        )