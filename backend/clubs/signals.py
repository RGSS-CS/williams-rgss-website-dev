from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Club, ClubWhyJoin, ClubAnnouncement
from management.revalidation import revalidate_frontend

@receiver(post_save, sender=Club)
@receiver(post_delete, sender=Club)
@receiver(post_save, sender=ClubWhyJoin)
@receiver(post_delete, sender=ClubWhyJoin)
@receiver(post_save, sender=ClubAnnouncement)
@receiver(post_delete, sender=ClubAnnouncement)
def on_club_change(sender, instance, **kwargs):
    revalidate_frontend("clubs")
