from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ListCreateProductView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ListSearchView(generics.ListAPIView):
  serializer_class = ProductSerializer

  def get_queryset(self):
    queryset = Product.objects.all()
    query = self.request.query_params.get('category')
    queryset = queryset.filter(category__iexact=query)
    return queryset