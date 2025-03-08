from django.views import View
from django.shortcuts import render
from .models import Currency, Rate

# Create your views here.
class RatesView(View):
    def get(self, request):
        value = None
        if 'currency_from' in request.GET and 'currency_to' in request.GET and 'amount' in request.GET:
            currency_from = request.GET["currency_from"]
            currency_to = request.GET["currency_to"]
            amount = float(request.GET["amount"])
            rate = Rate.objects.filter(
                currency_from__code=currency_from,
                currency_to__code=currency_to,
            ).order_by("-date").first()
            value = amount * rate.value
        currencies = Currency.objects.all()
        return render(request, "rates.html", {"currencies": currencies, "value": value})