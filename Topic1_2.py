#Yes, Django signals run in same thread as the caller

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"[Signal Handler] Signal running in thread ID : {threading.get_ident()} ")


def trigger_signal():
    print(f"[Caller] Function running in thread Id : {threading.get_ident()}")
    User.objects.create(username='user_a')

trigger_signal()


#By viewing the thread Id of both we can say that signal has run in same thread as the caller.