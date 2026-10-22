# services/recommendation_engine.py

from collections import Counter
from typing import List, Tuple
from repositories.base import BaseRepository

class RecommendationEngine:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def get_most_popular_authors(self) -> List[Tuple[str, int]]:
        """
        استخدام Counter لإيجاد أكثر المؤلفين تكراراً في المكتبة.
        """
        books = self.repo.get_all_books()
        
        # جمع كل أسماء المؤلفين
        authors = [book.author for book in books]
        
        # استخدام Counter لعد وترتيب المؤلفين
        author_counts = Counter(authors)
        
        # إرجاع أكثر 3 مؤلفين شيوعاً
        return author_counts.most_common(3)