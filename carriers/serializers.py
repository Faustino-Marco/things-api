from rest_framework import serializers
from .models import Carrier

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'trip', 'description', 'start_date', 'end_date')
        model = Carrier

