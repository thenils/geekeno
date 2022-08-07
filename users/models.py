from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from books.models import Books


class MyBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_reading_list')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='in_user_list')
    is_reading = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.name + ' ' + self.user.username

    class Meta:
        db_table = 'mybook'
        ordering = ['-id']
