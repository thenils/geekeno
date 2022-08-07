from django.contrib.auth.models import User

from books.models import Books
from users.models import MyBooks


class MyBookService:

    def __init__(self):
        self.model = MyBooks

    def get_mybook_list(self, user: User, data=None):
        return self.model.objects.filter(user=user, **data)

    def add_book_to_read_list(self, user: User, book: Books):
        return self.model.objects.create(user=user, book=book)

    def get_book(self, user: User, reading_book_id: int):
        return self.model.objects.filter(pk=reading_book_id, user=user)

    def update_reading_book(self, user: User, reading_book_id: int, data: dict):
        reading_book = self.model.objects.filter(pk=reading_book_id, user=user).first()
        if 'is_deleted' in data:
            reading_book.is_deleted = data['is_deleted']

        if 'is_reading' in data:
            reading_book.is_reading = data['is_reading']

        reading_book.save()
        return reading_book

    def book_exists(self, user: User, book: Books):
        return self.model.objects.filter(user=user, book=book).exists()
