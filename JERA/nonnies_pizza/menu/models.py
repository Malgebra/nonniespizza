from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
