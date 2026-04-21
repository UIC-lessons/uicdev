from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification

user = get_user_model()

@receiver(post_save, sender = user)
def welcome_notif(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user = instance,
            title = "Xush kelibsiz",
            message = f"Salom {instance.first_name}, UICdev platformasidan muvaffaqiaytli ro'yxatdan o'tdinggiz!",
            is_send_to_all = False
        )