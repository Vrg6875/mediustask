from django.contrib import admin
from news.models import VicNews  # Correct import statement

class VicAdmin(admin.ModelAdmin):  # Class name should follow PEP 8 conventions
    list_display = ('today_news', 'des')

admin.site.register(VicNews, VicAdmin)  # Register the correct model and admin class
