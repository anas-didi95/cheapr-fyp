from django.db import models
from django.contrib import admin

class Product(models.Model):
  CATEGORY_CHOICES = (
    ('snack', 'Snack'),
    ('drink', 'Drink'),
    ('fresh', 'Fresh Food'),
    ('toilet', 'Toiletries'),
    ('house', 'Household'),
    ('ingredient', 'Ingredient')
  )
  name = models.CharField(
    max_length=255, 
    unique=True,
  )
  category = models.CharField(
    max_length=255, 
    choices=CATEGORY_CHOICES,
  )
  thumbnail = models.ImageField(
    upload_to='thumbnails/',
    blank=True,
    default=''
  )
  date_created = models.DateTimeField(
    auto_now_add=True,
  )
  date_updated = models.DateTimeField(
    auto_now=True,
  )

  def __str__(self):
    return '%s' % (self.name)

class ProductAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'category',
    'date_updated',
  )

  list_filter = (
    'category',
  )

  search_fields = [
    'name',
  ]