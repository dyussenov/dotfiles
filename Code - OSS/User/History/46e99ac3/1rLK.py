from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    preview = models.ImageField()
    description = models.TextField()


class Question(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'blog_app.CustomUser',
        on_delete=models.CASCADE
    )
    body = models.TextField()


class Answer(models.Model):
    author = models.ForeignKey(
        'blog_app.CustomUser',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
