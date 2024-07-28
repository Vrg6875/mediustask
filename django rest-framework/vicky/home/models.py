from django.db import models




class ipl(models.Model):
 iplid=models.AutoField(primary_key=True)
 iplname=models.CharField(max_length=100)
 ipllocation=models.CharField(max_length=100)
 added_date=models.DateTimeField(auto_now=True)
 active=models.BooleanField(default=True)


class iplcolor(ipl):
  dresscolor=models.CharField(max_length=20)
