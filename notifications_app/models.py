from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class BroadcastNotification(models.Model):
    message = models.TextField()
    broadcast_on = models.DateTimeField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-broadcast_on']


@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    pass
