from rest_framework import serializers
from app.models import Company_data, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_data
        fields = '__all__'