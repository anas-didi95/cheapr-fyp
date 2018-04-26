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
    if query is None:
      query = self.request.query_params.get('name')
      query = query.split(' ')
      for q in query:
        queryset = queryset.filter(name__icontains=q)
    else:
      queryset = queryset.filter(category__iexact=query)
    return queryset