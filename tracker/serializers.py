from .models import Character, Payment
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ["name", "character_type"]


# class PaymentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Payment
#         fields = ["character", "amount", "date"]
