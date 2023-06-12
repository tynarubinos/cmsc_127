from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('food_item', 'Food Item'),
        ('non_food_item', 'Non-Food Item'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

class Product(models.Model):
    product_code = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_acquired = models.DateField()
    expiration_date = models.DateField()
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    storage_location = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
