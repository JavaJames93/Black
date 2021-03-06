from rest_framework import serializers
from app.models import DataFile


# DataFile serializer
class DataFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataFile
        fields = '__all__'