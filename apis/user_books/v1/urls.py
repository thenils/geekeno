from django.urls import path

from apis.user_books.v1.views import MyReadingViewSet

urlpatterns = [
    path('', MyReadingViewSet.as_view({'get': 'list', 'post': 'create'}), name='reading_list'),
    path('<int:reading_book_id>/', MyReadingViewSet.as_view({'get': 'retrieve', 'patch': 'update'}), name='reading-book-detail'),

]
