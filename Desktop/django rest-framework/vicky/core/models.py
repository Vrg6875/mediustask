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