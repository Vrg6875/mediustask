from django.db import models

class project_vic(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    des = models.TextField()
    another = models.TextField(default='your_default_value')
    goal=models.TextField(default='mera')
    founder= models.TextField(default='tera')
    vikash= models.TextField(default='kya')
   
