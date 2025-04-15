from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
