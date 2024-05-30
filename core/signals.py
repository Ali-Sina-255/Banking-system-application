from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    try:
        profile = UserProfile.objects.get(user=instance)
        profile.save()
        print('user profile is updated')

    except Exception as e:
        UserProfile.objects.create(user=instance)
        print('profile was not exists, but was created ')
    print("User is updated")


@receiver(pre_save,sender=User)
def per_save_profile_reciver(sender, instance, **kwargs):
    print(instance.username+ ' ' + 'this is being saved')
