from django.db import models
from tinymce.models import HTMLField
#from autoslug import AutoSlugField

# Correcting the import

class VicNews(models.Model):  # Updated class name to follow PEP 8 conventions
    today_news = models.TextField()
    des = HTMLField()
    #news_slug = AutoSlugField(populate_from="today_news", unique=True)
