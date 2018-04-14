from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
  path('', views.ListCreateSupermarketView.as_view(), name='supermarket.l-c'),
  path('<int:pk>', views.RetrieveUpdateDestroySupermarketView.as_view(), name='supermarket.r-u-d'),
]
urlpatterns = format_suffix_patterns(urlpatterns)