from rest_framework import generics
from .serializers import SupermarketSerializer
from .models import Supermarket

class ListCreateSupermarketView(generics.ListCreateAPIView):
  queryset = Supermarket.objects.all()
  serializer_class = SupermarketSerializer

class RetrieveUpdateDestroySupermarketView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Supermarket.objects.all()
  serializer_class = SupermarketSerializer