from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,permissions,status
from blog.render import UserRenderer
from .models import Categories,Tags,Blog,Comment
from rest_framework.response import Response
from blog.pagination import MyPageNumberPagination
from .serializer import (
    Catogeries_Serializer,
    Tage_Serializer,
    Blog_Serializer,
    Comment_Serializer,
    CommentCustom_Serializer,
)
#Catogeries.
#catogeries create view.
class CatogeriesCreateApiView(generics.CreateAPIView):
    renderer_classes = [UserRenderer]
    queryset = Categories.objects.all()
    serializer_class = Catogeries_Serializer

#catogeries list view.
class CatogeriesListApiView(generics.ListAPIView):
    renderer_classes = [UserRenderer]
    queryset = Categories.objects.all()
    serializer_class = Catogeries_Serializer

#catogeries update view.
class CatogeriesUpdateApiView(generics.UpdateAPIView):
    renderer_classes = [UserRenderer]
    queryset = Categories.objects.all()
    serializer_class = Catogeries_Serializer

#catogeries delete view.
class CatogeriesDeleteApiView(generics.DestroyAPIView):
    renderer_classes = [UserRenderer]
    queryset = Categories.objects.all()
    serializer_class = Catogeries_Serializer


#Tags.
#tags create view.
class TagsCreateApiView(generics.CreateAPIView):
    renderer_classes = [UserRenderer]
    queryset = Tags.objects.all()
    serializer_class = Tage_Serializer

#tags list view.
class TagsListApiView(generics.ListAPIView):
    renderer_classes = [UserRenderer]
    queryset = Tags.objects.all()
    serializer_class = Tage_Serializer

#tags delete view.
class TagsDeleteApiView(generics.DestroyAPIView):
    renderer_classes = [UserRenderer]
    queryset = Tags.objects.all()
    serializer_class = Tage_Serializer

#tags update view.
class TagsUpdateApiView(generics.UpdateAPIView):
    renderer_classes = [UserRenderer]
    queryset = Tags.objects.all()
    serializer_class = Tage_Serializer


#Blog
#blog create view.
class BlogCreateApiView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,*args, **kwargs):
        print("Incoming data from frontend:", request.data)
        serializer = Blog_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["author"] = request.user.name
            tags_data = request.data.get('tags', [])
            catogeries_data= request.data.get('categories', [])
            tag_instance = serializer.save()
            for cat_id in catogeries_data:
                cat=Categories.objects.get(id=cat_id)
                tag_instance.categories.add(cat)
            for tag_id in tags_data:
                tag = Tags.objects.get(id=tag_id)
                tag_instance.tags.add(tag)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
#blog list view.
class BlogListApiView(generics.ListAPIView):
    renderer_classes = [UserRenderer]
    queryset=Blog.objects.all().order_by("-id")
    serializer_class = Blog_Serializer
    pagination_class = MyPageNumberPagination


#Comment.
#comment create view.
class CommentCreateApiView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id, *args, **kwargs):
        blog = Blog.objects.get(pk=id)
        serializer = Comment_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["blog"] = blog
            serializer.validated_data["commented_by"]=request.user.name
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

# comment list view.
class CommentListApiView(generics.ListAPIView):
    serializer_class = CommentCustom_Serializer
    renderer_classes = [UserRenderer]
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        id = self.kwargs["id"]
        return Comment.objects.filter(blog=id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(
                queryset,
                many=True,
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                "No comments found for this blog",
                status=status.HTTP_404_NOT_FOUND,
            )