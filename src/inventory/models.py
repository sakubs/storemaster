from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=120)
    cost = models.DecimalField(decimal_places=2)
    price = models.DecimalField(decimal_places=2)
    category1 = models.CharField(max_length=120)
    category2 = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    description = models.TextField()
    condition = models.CharField(max_length=120)
    weight = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    material = models.CharField(max_length=120)


class Manga(Item):
    volume = models.CharField(max_length=10)
    print_date = models.DateField()
    publish_date = models.DateField()
    author = models.CharField(max_length=120)
