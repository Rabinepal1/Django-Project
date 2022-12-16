from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'description']
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ['category_name']

@admin.register(Post)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProjectSettings)
class AdminSetting(admin.ModelAdmin):
    pass