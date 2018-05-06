from rest_framework import generics
from .serializers import PriceSerializer
from .models import Price

class ListCreatePriceView(generics.ListCreateAPIView):
  queryset = Price.objects.all()
  serializer_class = PriceSerializer

class RetrieveUpdateDestroyPriceView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Price.objects.all()
  serializer_class = PriceSerializer

class ListFilterView(generics.ListAPIView):
  serializer_class = PriceSerializer

  def get_queryset(self):
    queryset = Price.objects.all()
    query_product = self.request.query_params.get('product')
    query_supermarket = self.request.query_params.get('supermarket')
    queryset = queryset.filter(
      product_id=query_product,
      supermarket_id=query_supermarket)
    return queryset
