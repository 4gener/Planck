from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'createTransfer', views.create_transfer, name='create_transfer'),
    url(r'getBalance', views.get_balance, name='get_balance'),
]
