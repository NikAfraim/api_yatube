from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента!')
        super(PostViewSet, self).perform_destroy(instance)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента!')
        super(PostViewSet, self).perform_update(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента!')
        super(CommentViewSet, self).perform_destroy(instance)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента!')
        super(CommentViewSet, self).perform_update(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
