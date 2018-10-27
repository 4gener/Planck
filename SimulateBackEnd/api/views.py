import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .serializers import *
from .models import *


@csrf_exempt
def create_transfer(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        address = data['address']
        spend_coin_id = data['spend_coin_id']
        receive_coin_id = data['receive_coin_id']
        spend_amount = data['spend_amount']

        account = Account.objects.get(address=address)
        spend_coin = Coin.objects.get(id=spend_coin_id)
        receive_coin = Coin.objects.get(id=receive_coin_id)

        connector = Connector()

        if spend_coin.is_ETH:
            connector = Connector.objects.get(deposit_coin=spend_coin, smart_coin=receive_coin)
        elif spend_coin.is_bancor:
            if receive_coin.is_ETH:
                connector = Connector.objects.get(smart_coin=spend_coin, deposit_coin=receive_coin)
            else:
                connector = Connector.objects.get(smart_coin=receive_coin, deposit_coin=spend_coin)

        if not account.is_balance_enough(spend_coin, spend_amount):
            return JsonResponse({
                'errmsg': '余额不足'
            }, status=400)

        transfer = account.create_transfer(connector, spend_amount,
                                           is_buying_smart=connector.smart_coin.id is receive_coin.id)

        return JsonResponse(TransferSerializer(transfer).data)
    else:
        return JsonResponse(None, status=400)
