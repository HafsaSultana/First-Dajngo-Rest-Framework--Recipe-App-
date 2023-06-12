from django.contrib import admin
from .models import RecipeDetail, Category_Tag, TagList
# Register your models here.

admin.site.register(RecipeDetail)
admin.site.register(Category_Tag)
admin.site.register(TagList)
