from django.contrib import admin
from cgc.models import vic_cgc

class admin_vic(admin.ModelAdmin):
    list_display=('student_name','roll_no','section')
admin.site.register(vic_cgc,admin_vic)    

# Register your models here.
