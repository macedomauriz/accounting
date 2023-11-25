from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"character", views.CharactersViewSet)

urlpatterns = [
    # index is the name of the def view
    path("<int:number>", views.detail, name="detail"),
    # drf routes
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
