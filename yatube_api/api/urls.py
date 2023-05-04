from rest_framework.routers import SimpleRouter
from django.urls import include, path
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = SimpleRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
