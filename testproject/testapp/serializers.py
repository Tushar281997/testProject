from rest_framework import serializers
from .models import VendorMaster

class VendorMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorMaster
        fields = '__all__'  # Include all fields from the model
