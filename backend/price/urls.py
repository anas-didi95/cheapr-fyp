from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('', views.ListCreatePriceView.as_view(), name='price.l-c'),
  path('<int:pk>', views.RetrieveUpdateDestroyPriceView.as_view(), name='price.r-u-d'),
  path('filter', views.ListFilterView.as_view(), name='price-filter.l'),
]
urlpatterns = format_suffix_patterns(urlpatterns)