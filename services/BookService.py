from books.models import Books


class BookService:
    def __init__(self):
        self.model = Books

    def list_book(self):
        return self.model.objects.all()

    def get_book(self, book_id: int):
        return self.model.objects.filter(pk=book_id)

    def create_book(self, name: str, author: str):
        return self.model.objects.create(name=name, author=author)
