import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from web.models import Currency, Rate


class Command(BaseCommand):
    help = "Download currency rates"

    def handle(self, *args, **options):
        print("Downloading currency rates...")
        url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()
        date = lines[0].split()[0]
        date = datetime.strptime(date, "%d.%m.%Y").date()
        # chek if rates for this date are already downloaded
        if Rate.objects.filter(date=date).exists():
            print(f"Rates for {date} already downloaded")
            return
        czk_code = "CZK"
        czk_currency = Currency.objects.get(code=czk_code)
        for line in lines[2:]:
            parts = line.split("|")
            code = parts[3]
            currency = Currency.objects.filter(code=code).first()
            if not currency:
                print(f"Currency {code} not found")
                continue
            rate = float(parts[4].replace(",", ".")) / int(parts[2])
            Rate.objects.create(
                currency_from=czk_currency,
                currency_to=currency,
                date=date,
                value=1 / rate,
            )
            Rate.objects.create(
                currency_from=currency,
                currency_to=czk_currency,
                date=date,
                value=rate,
            )
            print(f"{czk_code} - {code} - {rate}")
