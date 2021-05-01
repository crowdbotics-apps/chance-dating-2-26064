from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    InboxViewSet,
    SettingViewSet,
    DislikeViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("setting", SettingViewSet)
router.register("match", MatchViewSet)
router.register("inbox", InboxViewSet)
router.register("profile", ProfileViewSet)
router.register("userphoto", UserPhotoViewSet)
router.register("like", LikeViewSet)
router.register("dislike", DislikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
