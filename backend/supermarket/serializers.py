from rest_framework import serializers
from .models import Supermarket

class SupermarketSerializer(serializers.ModelSerializer):
  """Serialize model Supermarket into JSON format"""

  class Meta:
    model = Supermarket
    fields = (
      'id',
      'name',
      'date_created',
      'date_updated',
    )
    read_only_fields = (
      'date_created',
      'date_updated',
    )
