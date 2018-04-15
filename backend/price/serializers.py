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
      'date_start',
      'date_end',
      'description',
      'product',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )
