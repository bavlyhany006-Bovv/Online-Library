from abc import ABC, abstractmethod
from typing import List, Optional
from models.user import User
from models.book import Book

class BaseRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None: pass
    
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]: pass
    
    @abstractmethod
    def get_all_users(self) -> List[User]: pass
    
    @abstractmethod
    def save_book(self, book: Book) -> None: pass
    
    @abstractmethod
    def get_book_by_id(self, book_id: int) -> Optional[Book]: pass
    
    @abstractmethod
    def get_all_books(self) -> List[Book]: pass