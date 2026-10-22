# services/library_service.py

from typing import List
from models.user import User
from models.book import Book
from repositories.base import BaseRepository
from utils.exceptions import NotFoundError, ValidationError

class LibraryService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def add_user(self, name: str, email: str) -> User:
        """إضافة مستخدم جديد للنظام."""
        users = self.repo.get_all_users()
        new_id = len(users) + 1  # توليد ID بسيط
        new_user = User(user_id=new_id, name=name, email=email)
        self.repo.save_user(new_user)
        return new_user

    def add_book(self, title: str, author: str, category_id: int, copies: int) -> Book:
        """إضافة كتاب جديد."""
        books = self.repo.get_all_books()
        new_id = len(books) + 1
        new_book = Book(book_id=new_id, title=title, author=author, category_id=category_id, available_copies=copies)
        self.repo.save_book(new_book)
        return new_book

    def search_books(self, query: str) -> List[Book]:
        """البحث عن الكتب بالاسم أو المؤلف."""
        books = self.repo.get_all_books()
        query = query.lower()
        return [b for b in books if query in b.title.lower() or query in b.author.lower()]

    def borrow_book(self, user_id: int, book_id: int) -> bool:
        """عملية استعارة كتاب وتطبيق قواعد البيزنس."""
        user = self.repo.get_user_by_id(user_id)
        book = self.repo.get_book_by_id(book_id)

        if not user:
            raise NotFoundError("User not found in the system.")
        if not book:
            raise NotFoundError("Book not found.")
        
        # التأكد من وجود نسخ متاحة قبل الاستعارة
        if book.available_copies <= 0:
            raise ValidationError(f"No available copies for '{book.title}' right now.")

        # تقليل عدد النسخ المتاحة بمقدار 1
        book.available_copies -= 1
        self.repo.save_book(book)
        
        # (في الخطوات القادمة سنقوم بتسجيل الاستعارة في ملف ReadingHistory)
        return True