from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ListCreateProductView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer