from django.db import models

class Price(models.Model):
  price_value = models.DecimalField(
    max_digits=6,
    decimal_places=2,
  )
  currency_value = models.DecimalField(
    max_digits=6,
    decimal_places=2,
  )
  date_start = models.CharField(max_length=255)
  date_end = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  product = models.ForeignKey(
    'product.Product',
    on_delete=models.CASCADE
  )