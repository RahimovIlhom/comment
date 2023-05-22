from rest_framework import routers
from comment.views import CommentViewSet, NegativeCommentViewSet, PositiveCommentViewSet, DiniyCommentViewSet, \
    TerrorCommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'negative-comments', NegativeCommentViewSet, basename='negative-comment')
router.register(r'positive-comments', PositiveCommentViewSet, basename='positive-comment')
router.register(r'diniy-comments', DiniyCommentViewSet, basename='diniy-comment')
router.register(r'terroristik-comments', TerrorCommentViewSet, basename='terror-comment')