from django.db import models


class Account(models.Model):
    address = models.CharField(max_length=42, default='', primary_key=True)

    def is_balance_enough(self, coin, value):
        return Balance.objects.get(address=self, coin=coin).value >= value

    def create_transfer(self, connector, spend_amount, is_buying_smart):
        spend_coin = connector.deposit_coin if is_buying_smart else connector.smart_coin
        receive_coin = connector.smart_coin if is_buying_smart else connector.deposit_coin
        receive_amount = connector.calculate_smart(spend_amount) if is_buying_smart else connector.calculate_deposit(
            spend_amount)

        connector.update_with_transfer(spend_amount, is_buying_smart)
        connector.save()

        transfer = Transfer(from_account=self,
                            to_connector=connector,
                            spend_coin=spend_coin,
                            receive_coin=receive_coin,
                            spend_amount=spend_amount,
                            receive_amount=receive_amount)
        transfer.save()

        spend_balance = Balance.objects.get(coin=spend_coin, address=self)
        receive_balance = Balance.objects.get(coin=receive_coin, address=self)

        spend_balance.value -= spend_amount
        receive_balance.value += receive_amount
        spend_balance.save()
        receive_balance.save()

        return transfer


class Coin(models.Model):
    name = models.CharField(max_length=10, default='')
    is_bancor = models.BooleanField(default=False)
    is_ETH = models.BooleanField(default=False)


class Balance(models.Model):
    address = models.ForeignKey(Account, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)


class CoinPriceLog(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    value_by_ETH = models.FloatField(default=0.0)
    change_rate = models.FloatField(default=0.0)


class Connector(models.Model):
    smart_coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='smart_coin')
    deposit_coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='deposit_coin')
    cw = models.FloatField(default=0.0)  # 连接器权重
    before_price = models.FloatField(default=0.0)  # 交易前价格
    after_price = models.FloatField(default=0.0)  # 交易后价格
    deposit = models.IntegerField(default=0)  # 储备金额
    circulation = models.IntegerField(default=0)  # 流通量

    def calculate_smart(self, receive_value):
        result = self.circulation * ((1 + receive_value / self.deposit) ** self.cw - 1.0)
        return int(result)

    def calculate_deposit(self, receive_value):
        result = self.deposit * ((1 + receive_value / self.circulation) ** (1 / self.cw) - 1)
        return int(result)

    def update_with_transfer(self, receive_value, is_buying_smart):
        result = self.calculate_smart(receive_value) if is_buying_smart else self.calculate_deposit(receive_value)
        print(result)
        self.before_price = receive_value / result if is_buying_smart else result / receive_value
        self.after_price = (self.deposit + receive_value) / (
                self.cw * (self.circulation - result)) if is_buying_smart else (self.deposit + result) / (
                self.cw * (self.circulation - receive_value))
        self.deposit = self.deposit + receive_value if is_buying_smart else self.deposit - result
        self.circulation = self.circulation + result if is_buying_smart else self.circulation - receive_value


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    to_connector = models.ForeignKey(Connector, on_delete=models.CASCADE)
    spend_coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='spend_coin')
    receive_coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='receive_coin')
    spend_amount = models.IntegerField(default=0)
    receive_amount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
