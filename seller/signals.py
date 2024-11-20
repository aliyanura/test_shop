from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Seller

@receiver(post_save, sender=Seller)
def notify_users_on_seller_creation(sender, instance, created, **kwargs):
    if created:
        message = f"New seller created: {instance.user.username}!"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": message,
            }
        )
