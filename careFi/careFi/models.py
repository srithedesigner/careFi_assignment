from statistics import mode
from django.db import models

class bitCoinPrice(models.Model):
    time = models.DateTimeField()
    price = models.FloatField()
    
    def __str__(self):
        return f"The price of Bitcoin at {self.time}"