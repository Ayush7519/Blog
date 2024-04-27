from django.urls import path
from . import views

urlpatterns = [
    path(
        "login/",
        views.UserLoginView.as_view(),
        name="path to login user",
    )
]
