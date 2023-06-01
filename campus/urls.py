from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("display/", views.display_students, name="display_students"),
    # path("students/", views., name="view_students"),
]
