from rest_framework import serializers

from .models import *


class TransferSerializer(serializers.ModelSerializer):
    """
     TransferSerializer 类的默认 Serializer，它包含了全部属性
    """

    class Meta:
        model = Transfer
        fields = '__all__'
