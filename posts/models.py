from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f'Author: {seld.author} | Body: {self.body}'