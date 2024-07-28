from django.contrib import admin
from project.models import project_vic

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'des','another','goal','founder')

admin.site.register(project_vic, ServiceAdmin)
