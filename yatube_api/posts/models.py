from django.contrib.auth import get_user_model
from django.db import models

from .abstract_models import CreatedModel

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(CreatedModel):
    text = models.TextField()
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        default=''
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return f'{self.text[:30]}'


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()


class Follow(CreatedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
