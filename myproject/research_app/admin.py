from django.contrib import admin
from .models import ProjectModel, TagModel

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('created_time', 'updated_time', 'created_by', 'updated_by')
admin.site.register(TagModel, TagAdmin)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'author_name', 'project_date', 'display_tags', 'image', 'pdf_file', )
    filter_horizontal = ('project_tag',)
    readonly_fields = ('created_time', 'updated_time', 'created_by', 'updated_by')

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.project_tag.all())
    display_tags.short_description = "Tags"

admin.site.register(ProjectModel, ProjectModelAdmin)
