from django.db import models

class vic_ipl(models.Model):
    team_name=models.CharField(max_length=50)
    location_no=models.TextField()
    ipl_image=models.ImageField(upload_to="ipl",default='')