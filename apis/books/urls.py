from django.urls import path, include

urlpatterns = [
    path('v1/', include('apis.books.v1.urls'))
]