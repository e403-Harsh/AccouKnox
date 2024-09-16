#By default Django signals are executed synchronously

import time,datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"[Signal Handler] Signal received at {datetime.datetime.now()}")
    time.sleep(5)
    print(f"[Signal Handler] Signal processing complete.")


def trigger_signal():
    print(f"[Caller] Creating user at {datetime.datetime.now()}")
    User.objects.create(username='user_a')
    print(f"[Caller] User created at {datetime.datetime.now()}")

trigger_signal()


#Signals are executed synchronously, As the calling function waits for processing complete to create the user.