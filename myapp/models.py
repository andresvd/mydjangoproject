from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class List(models.Model):
    list_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.list_title

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    deadline = models.DateField('deadline', default=None)
    orderNumber = models.IntegerField(default=1)

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.item_text

