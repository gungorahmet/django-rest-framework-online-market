from django.db import models




# The model is just for initiating, surely will be changed with a good design
class Product(models.Model):
    title          = models.CharField(max_length=100)
    product_name   = models.CharField(max_length=100)
    description    = models.CharField(max_length=500)
    product_type   = models.CharField(max_length=20)
    price          = models.FloatField()
    stock_count    = models.PositiveIntegerField()
    guarantee      = models.PositiveSmallIntegerField()
    shipping_price = models.FloatField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
