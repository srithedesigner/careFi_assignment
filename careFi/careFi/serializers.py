from dataclasses import fields
from rest_framework import serializers
from .models import bitCoinPrice

class  BitcoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = bitCoinPrice
        fields = ['id', 'time', 'prices']
        
    