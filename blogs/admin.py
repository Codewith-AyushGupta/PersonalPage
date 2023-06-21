from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import blogs_database,loogin_data,BlogComments,project

@admin.register(blogs_database)
@admin.register(loogin_data)
@admin.register(BlogComments)

class projectAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(project,projectAdmin)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tiny.js',)
