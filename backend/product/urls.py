from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('', views.ListCreateProductView.as_view(), name='product.l-c'),
  path('<int:pk>', views.RetrieveUpdateDestroyProductView.as_view(), name='product.r-u-d'),
  path('search', views.ListSearchView.as_view(), name='product-search.l'),
]
urlpatterns = format_suffix_patterns(urlpatterns)