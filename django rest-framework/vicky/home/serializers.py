from rest_framework import serializers
from .models import*


class iplserializers(serializers.ModelSerializer):
    class Meta:
        model = ipl
        fields = '__all__'

class iplcolorserializers(serializers.ModelSerializer):
    class Meta:
        model = iplcolor
        fields = '__all__'