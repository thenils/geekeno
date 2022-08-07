from django.contrib import admin

# Register your models here.
from users.models import MyBooks

admin.site.register(MyBooks)
