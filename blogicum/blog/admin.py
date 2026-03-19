from django.contrib import admin

from .models import Location, Category, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'is_published',
    )
    list_editable = (
        'is_published',
    )


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'created_at',
        'is_published',
        'author',
        'category',
        'location',
    )
    list_editable = (
        'is_published',
        'author',
        'category',
        'location',
    )
    search_fields = ('title',)
    list_filter = ('category', 'author', 'location',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
