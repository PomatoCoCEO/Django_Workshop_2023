from django.db import models

# Create your models here.

# create a product model with name, price, and quantity
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

# create a user model
class User(models.Model):
    # the user has to be unique to avoid problems like the ones we had
    # in the workshop (:
    username = models.CharField(max_length=100, unique=True)
    # make sure to delete the redundant users before migrating the database
    password = models.CharField(max_length=100)
    balance = models.FloatField(default=1000)
    bought_products = models.ManyToManyField(Product, blank=True)
    
    def __str__(self):
        return self.name