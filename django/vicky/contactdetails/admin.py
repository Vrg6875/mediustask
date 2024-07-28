from django.contrib import admin
from contactdetails.models import vic_contactdetails

class vic_admin(admin.ModelAdmin):
    list_display=('name','phone','message')
admin.site.register(vic_contactdetails,vic_admin)    


# Register your models here.
