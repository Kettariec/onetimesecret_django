from django.urls import path
from onetimesecret.views import SecretCreateView, SecretGetView
from onetimesecret.apps import OnetimesecretConfig

app_name = OnetimesecretConfig.name


urlpatterns = [
    path('', SecretCreateView.as_view(), name='index'),
    path('secret/<str:code>/', SecretGetView.as_view(), name='secret_page'),
    ]
