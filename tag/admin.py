from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import Tag 


class CategoryAdmin(admin.ModelAdmin):
    ...


class TagInline(GenericStackedInline):
    model = Tag
    fields = 'name',
    extra = 1
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'id', 'slug', 
    list_per_page = 10
    list_editable = 'name',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
        }

    inlines = [
        TagInline,
    ]