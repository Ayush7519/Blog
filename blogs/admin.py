from django.contrib import admin
from .models import Categories,Tags,Blog,Comment


#registring the catogery model in the admin.
class Catogeries_Admin(admin.ModelAdmin):
    list_display=('id',"type","date_created","date_updated")
admin.site.register(Categories,Catogeries_Admin)

#Tags model registrations.
class Tags_Admin(admin.ModelAdmin):
    list_display=('id','tage_name','date_created','date_updated')

admin.site.register(Tags,Tags_Admin)

#Blog model registration.
class Blog_Admin(admin.ModelAdmin):
    list_display=('id','title','content','author')

admin.site.register(Blog,Blog_Admin)

#comment model registration.
class Comment_Admin(admin.ModelAdmin):
    list_display=('id','commented_by','commented_content','blog')

admin.site.register(Comment,Comment_Admin)