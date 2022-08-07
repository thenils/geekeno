from django.urls import path, include

urlpatterns = [
    path('auth/', include('apis.authentication.urls')),
    path('book/', include('apis.books.urls')),
    path('mybook/', include('apis.user_books.urls'))
]