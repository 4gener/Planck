from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'createTransfer', views.create_transfer, name='create_transfer'),
]
