from django.db import models
from .base import BaseModel

#defining the model for the catogeries.
class Categories(BaseModel):
    type=models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return self.type

#defining the model for the tags.
class Tags(BaseModel):
    tage_name=models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return self.tage_name
    

#defining the model for the blogs.
class Blog(BaseModel):
    title = models.CharField(max_length=100,blank=False,null=False)
    content = models.TextField(blank=False,null=False)
    categories = models.ManyToManyField(Categories,blank=True,null=True)
    tags = models.ManyToManyField(Tags)
    author = models.CharField(max_length=20,blank=True, null=True)


    def __str__(self):
        return self.title
    

#defining the model for the comment.
class Comment(BaseModel):
    commented_by = models.CharField(max_length=10,blank=True,null=True)
    commented_content = models.CharField(max_length=100,blank=False,null=False)
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.commented_by