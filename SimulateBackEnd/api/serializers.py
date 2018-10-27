from rest_framework import serializers

from .models import *


class TransferSerializer(serializers.ModelSerializer):
    """
    Transfer 类的默认 Serializer，它包含了全部属性
    """

    class Meta:
        model = Transfer
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    """
    Coin 类的默认 Serializer，它包含了全部属性
    """

    class Meta:
        model = Coin
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    """
    Balance 类的默认 Serializer，它包含了全部属性
    """

    coin = CoinSerializer()

    class Meta:
        model = Balance
        fields = '__all__'


class ConnectorSerializer(serializers.ModelSerializer):
    """
    Connector 类的默认 Serializer，它包含了全部属性
    """

    deposit_coin = CoinSerializer()
    smart_coin = CoinSerializer()

    class Meta:
        model = Connector
        fields = '__all__'
