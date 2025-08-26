from django.db.models.signals import post_save
from django.dispatch import receiver
from history.models import History
from tweets.models import Tweet

@receiver(post_save, sender=Tweet)
def create_history_on_tweet(sender, instance, created, **kwargs):
    if created:
        summary = f"User {instance.user.username} Created tweet with a content of \"{instance.content}\" at {instance.created_at}"
        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,
            summary = f"User {instance.user.username} Created tweet with a content of \"{instance.content}\" at {instance.created_at}"

        )
