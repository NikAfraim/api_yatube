from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_version1 = DefaultRouter()
router_version1.register('posts', PostViewSet, basename='posts')
router_version1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                         basename='comments')
router_version1.register('groups', GroupViewSet, basename='groups')
router_version1.register('follows', FollowViewSet, basename='follows'),
# router_version1.register(r'(?P<username>\d+)/follow/', FollowViewSet,
#                          basename='follow'),
#         'profile/<str:username>/unfollow/',
#         views.profile_unfollow,
#         name='profile_unfollow'
#     ),

urlpatterns = [
    path('v1/', include(router_version1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
