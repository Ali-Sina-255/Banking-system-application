from django.db.models.signals import post_save

from accounts.models import Account
from .models import UserAccount


def create_user_account(sender, created, instance, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)
    try:
    
    except Exception as e:
        raise e

def save_user_account(sender, instance, **kwargs):
    instance.useraccount.save()


post_save.connect(create_user_account, sender=Account)
post_save.connect(save_user_account, sender=Account)
