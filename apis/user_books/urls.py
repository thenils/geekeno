from django.urls import path, include

urlpatterns = [
    path('v1/', include('apis.user_books.v1.urls'))
]