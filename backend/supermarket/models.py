from django.db import models

class Supermarket(models.Model):
  """Model for Supermarket"""
  name = models.CharField(max_length=255, blank=False, unique=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '%s' % (self.name);