from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=10) #by default age nahi data dalne pe 10 aayega 
    fathersname=models.CharField(max_length=100)


class section(student):
    group=models.CharField(max_length=100)




class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=88)

import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class todo(BaseModel):
    todo_title=models.CharField(max_length=100)
    todo_desc=models.TextField()
    is_done=models.BooleanField(default=False)




class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100) 
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('it','it'),('non it','non it')))
                                        
    added_date=models.DateTimeField(auto_now=True)

    active=models.BooleanField(default=True)