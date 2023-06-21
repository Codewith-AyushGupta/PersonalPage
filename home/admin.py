from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import project
# admin.site.register(project)


# @admin.register(loogin_data)
# admin.site.register(blogs_database)
# admin.site.register(loogin_data)
class projectAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'short_about', 'short_about','short_aboutshort_about','decription','image','status','date_time']

admin.site.register(project,projectAdmin)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tiny.js',)