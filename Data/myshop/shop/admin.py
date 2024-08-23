from django.contrib import admin
from .models import Shop, Tag

# Registering the Tag model
admin.site.register(Tag)

# Customizing the Shop admin interface
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_tags')  # Display these fields in the list view
    search_fields = ('name', 'tags__name')  # Allow search by shop name and tag name
    filter_horizontal = ('tags',)  # Use horizontal filter widget for ManyToManyField

    # Method to display tags in the list view
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'  # Set the column header in the admin list view
