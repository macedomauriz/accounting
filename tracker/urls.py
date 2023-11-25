from django.urls import path
from . import views

urlpatterns = [
    # index is the name of the def view
    path("", views.index, name="index"),
    path("<int:number>", views.detail, name="detail"),
]
