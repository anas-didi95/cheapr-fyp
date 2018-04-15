from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('', views.ListCreatePriceView.as_view(), name='price.l-c'),
  path('<int:pk>', views.RetrieveUpdateDestroyPriceView.as_view(), name='price.r-u-d'),
]
urlpatterns = format_suffix_patterns(urlpatterns)