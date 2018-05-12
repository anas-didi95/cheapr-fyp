from django.db import models
from django.contrib import admin

class Price(models.Model):
  price_value = models.DecimalField(
    max_digits=6,
    decimal_places=2,
  )
  currency_value = models.DecimalField(
    max_digits=6,
    decimal_places=2,
  )
  description = models.CharField(max_length=255)
  day_start = models.IntegerField(default=-1)
  day_end = models.IntegerField(default=-1)
  month_start = models.IntegerField(default=-1)
  month_end = models.IntegerField(default=-1)
  year_start = models.IntegerField(default=-1)
  year_end = models.IntegerField(default=-1)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  product = models.ForeignKey(
    'product.Product',
    on_delete=models.CASCADE,
    related_name='prices',
  )
  supermarket = models.ForeignKey(
    'supermarket.Supermarket',
    on_delete=models.CASCADE,
    related_name='prices',
    default='1',
  )

  class Meta:
    ordering = ['-year_start', '-month_start', '-day_start', '-description']

  def __str__(self):
    return '%s | %s | %s' % (self.supermarket.name, self.product.name, self.description)

class PriceAdmin(admin.ModelAdmin):
  list_display = (
    'product',
    'supermarket',
    'description',
    'date_updated',
  )

  list_filter = (
    'supermarket',
  )

  search_fields = [
    'product__name',
  ]