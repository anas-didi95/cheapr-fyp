from rest_framework import serializers
from .models import Price

class PriceSerializer(serializers.ModelSerializer):
  """Serialize model Price into JSON format"""
  
  class Meta:
    model = Price
    fields = (
      'id',
      'price_value',
      'currency_value',
      'day_start',
      'day_end',
      'month_start',
      'month_end',
      'year_start',
      'year_end',
      'description',
      'product',
      'supermarket',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )
