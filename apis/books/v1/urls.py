from django.urls import path

from apis.books.v1.views import BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('<int:book_id>/', BookViewSet.as_view({'get': 'retrieve'}), name='book-detail'),
]