from django.contrib import admin
from event.models import vic_event
class vic_admin(admin.ModelAdmin):
    list_display=('event_name', 'event_date', 'event_time', 'event_location', 'event_description', 'event_category', 'guests')
admin.site.register(vic_event,vic_admin)   

