from django.contrib import admin
from .models import Price, PriceAdmin

admin.site.register(Price, PriceAdmin)