from django.contrib import admin
from .models import *
# Register your models here.

class PostSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class CategorySlug(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
    
admin.site.register(Post, PostSlug)

admin.site.register(CategoryPage, CategorySlug)