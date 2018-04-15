from rest_framework import generics
from .serializers import PriceSerializer
from .models import Price

class ListCreatePriceView(generics.ListCreateAPIView):
  queryset = Price.objects.all()
  serializer_class = PriceSerializer

class RetrieveUpdateDestroyPriceView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Price.objects.all()
  serializer_class = PriceSerializer