from django.urls import path
from . import views

urlpatterns = [
    path(
        "cat/create/",
        views.CatogeriesCreateApiView.as_view(),
        name=" catogeries create path",
    ),
    path(
        "cat/list/",
        views.CatogeriesListApiView.as_view(),
        name=" catogeries create path",
    ),
    path(
        "cat/update/<int:pk>/",
        views.CatogeriesUpdateApiView.as_view(),
        name=" catogeries create path",
    ),
    path(
        "cat/delete/<int:pk>/",
        views.CatogeriesDeleteApiView.as_view(),
        name=" catogeries create path",
    ),
    path(
        "tag/create/",
        views.TagsCreateApiView.as_view(),
        name=" tags create path",
    ),
    path(
        "tag/list/",
        views.TagsListApiView.as_view(),
        name=" tags list path",
    ),
    path(
        "tag/delete/<int:pk>/",
        views.TagsDeleteApiView.as_view(),
        name=" tag delete path",
    ),
    path(
        "tag/update/<int:pk>/",
        views.TagsUpdateApiView.as_view(),
        name=" tag update path",
    ),
    path(
        "blog/create/",
        views.BlogCreateApiView.as_view(),
        name="path to create the blog",
    ),
    path(
        "blog/list/",
        views.BlogListApiView.as_view(),
        name="blog list path",
    ),
    path(
        "comment/create/<int:id>/",
        views.CommentCreateApiView.as_view(),
        name="path to create the comment in the blog",
    ),
    path(
        "comment/read/<int:id>/",
        views.CommentListApiView.as_view(),
        name="path to read the comment based on the blog id.",
    ),
]
