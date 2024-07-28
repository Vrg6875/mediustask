from django.db import models

class vic_cgc(models.Model):
    student_name=models.CharField(max_length=50)
    roll_no=models.TextField()
    section=models.CharField(max_length=10)