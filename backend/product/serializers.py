from rest_framework import serializers
from price.serializers import PriceSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  """Serialize model Product into JSON format"""
  category_name = serializers.CharField(
    source='get_category_display',
    read_only=True,
  )

  class Meta:
    model = Product
    fields = (
      'id',
      'name',
      'category',
      'category_name',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )