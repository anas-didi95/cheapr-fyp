from django.contrib import admin
from .models import Supermarket, SupermarketAdmin

admin.site.register(Supermarket, SupermarketAdmin)