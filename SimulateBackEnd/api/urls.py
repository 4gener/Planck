from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'createTransfer', views.create_transfer, name='create_transfer'),
    url(r'getBalance', views.get_balance, name='get_balance'),
    url(r'getConnector', views.get_connector, name='get_connector'),
    url(r'getRate', views.get_rate, name='get_rate'),
    url(r'getPriceLog', views.getCoinPriceLog, name='getPriceLog')
]
