from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_version1 = DefaultRouter()
router_version1.register('posts', PostViewSet, basename='posts')
router_version1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                         basename='comments')
router_version1.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router_version1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]