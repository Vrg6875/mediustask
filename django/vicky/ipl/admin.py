from django.contrib import admin
from ipl.models import vic_ipl

class admin_vic(admin.ModelAdmin):
    list_display=('team_name','location_no','ipl_image')
admin.site.register(vic_ipl,admin_vic)    

# Register your models here.
