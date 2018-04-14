from rest_framework import serializers
from supermarket.models import Supermarket
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  """Serialize model Product into JSON format"""
  category_name = serializers.CharField(
    source='get_category_display',
    read_only=True,
  )
  supermarket = serializers.SlugRelatedField(
    many=False,
    read_only=False,
    queryset=Supermarket.objects.all(),
    slug_field='name',
  )

  class Meta:
    model = Product
    fields = (
      'id',
      'name',
      'category',
      'category_name',
      'supermarket',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )