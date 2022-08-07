from django.db import models


# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=135, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'books'
        ordering = ['-id']
