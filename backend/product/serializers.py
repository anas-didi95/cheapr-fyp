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
      'thumbnail',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )

class ProductPriceSerializer(serializers.ModelSerializer):
  """Serialize model Product into JSON format with Price model"""
  category_name = serializers.CharField(
    source='get_category_display',
    read_only=True,
  )
  prices = PriceSerializer(many=True, read_only=True)

  class Meta:
    model = Product
    fields = (
      'id',
      'name',
      'category',
      'category_name',
      'thumbnail',
      'prices',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated'
    )