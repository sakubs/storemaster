from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=120)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category1 = models.CharField(max_length=120)
    category2 = models.CharField(blank=True, max_length=120)
    brand = models.CharField(blank=True, max_length=120)
    description = models.TextField()
    condition = models.CharField(max_length=120)
    weight = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    material = models.CharField(max_length=120)

    # Manga specific fields.
    volume = models.CharField(blank=True, max_length=10)
    print_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    author = models.CharField(blank=True, max_length=120)
