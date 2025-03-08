from django.contrib import admin
from .models import Currency, Rate

# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "symbol")
    search_fields = ("name", "code")

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ("date", "currency_from__code", "currency_to__code", "value")
    list_filter = ("currency_from__code", "currency_to__code")