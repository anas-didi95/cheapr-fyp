from django.db import models

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
  supermarket = models.ForeignKey(
    'supermarket.Supermarket',
    on_delete=models.CASCADE,
  )
  date_created = models.DateTimeField(
    auto_now_add=True,
  )
  date_updated = models.DateTimeField(
    auto_now=True,
  )

  def __str__(self):
    return '%s' % (self.name)
