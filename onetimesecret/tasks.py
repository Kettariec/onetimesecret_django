from celery import shared_task
from datetime import datetime
from onetimesecret.models import Secret
import pytz
from django.conf import settings


@shared_task
def check_secrets():
    """Periodically checks the secret lifetime
    and deletes secrets whose time has expired"""
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)

    secrets = Secret.objects.filter(time__lte=now)

    for secret in secrets:
        secret.delete()
