#Yes, Django signals run in the same database transaction as the caller.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"[Signal Handler] Signal sees username : {instance.username}")


def trigger_signal():
    with transaction.atomic():
        print(f"[Caller] Starting transaction")
        user=User.objects.create(username='user_a')
        print(f"[Caller] User created with username: {user.username}")

trigger_signal()


#As the signal handler able to see the username, we can say that the signals run in the same database transaction as the caler.