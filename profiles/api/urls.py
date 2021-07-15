from django.urls import path, include
from rest_framework.routers import DefaultRouter #sam kreira endpointe
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

#profile_list = ProfileViewSet.as_view({"get": "list"})
#profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

#urlpatterns = [
#    path("profiles/", profile_list, name="profile-list"),
#    path("profiles/<int:pk>/", profile_detail, name="profile-detail")
#]

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet) # r znači raw string
router.register(r"status", ProfileStatusViewSet, basename="status")

urlpatterns = [
    path("", include(router.urls)), #isti linkovi
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]