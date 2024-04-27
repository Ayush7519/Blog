from rest_framework import serializers
from .models import Categories,Tags,Blog,Comment

#serializer for the catogeries.
class Catogeries_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

#serializer for the tags model.
class Tage_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields= "__all__"

#serializer for the blog.
class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields ="__all__"
        depth = 1

# serializer for the comment create.
class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

# serializer for the custom comment.
class CommentCustom_Serializer(serializers.ModelSerializer):
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "commented_by",
            "commented_content",
            "date_created",
            "date_updated",
            "blog",
        )

    def get_date_created(self, obj):
        return {
            "date": obj.date_created.strftime("%Y-%m-%d"),
            "time": obj.date_created.strftime("%H:%M:%S"),
        }

    def get_date_updated(self, obj):
        return {
            "date": obj.date_created.strftime("%Y-%m-%d"),
            "time": obj.date_created.strftime("%H:%M:%S"),
        }