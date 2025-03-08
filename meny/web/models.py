from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1, blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Currencies"


class Rate(models.Model):
    currency_from = models.ForeignKey(Currency, related_name="currency_from", on_delete=models.CASCADE)
    currency_to = models.ForeignKey(Currency, related_name="currency_to", on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.currency_from} - {self.currency_to} - {self.date} - {self.value}"