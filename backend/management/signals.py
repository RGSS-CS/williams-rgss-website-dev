from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .revalidation import revalidate_frontend
 
from .models import PageSettings, SiteSettings
 
def on_post_migrate(sender, app_config, *args, **kwargs):
    if not PageSettings.objects.filter(internal_site_name="AB").exists():
        PageSettings.objects.create(
            internal_site_name="AB",
            title="About STUCO",
            subtitle="",
            tagline="What about it? It's the student council..."
        )

    if not PageSettings.objects.filter(internal_site_name="GL").exists():
        PageSettings.objects.create(
            internal_site_name="GL",
            title="Gallery",
            subtitle="",
            tagline="Capturing the moments that matter most"
        )

    if not PageSettings.objects.filter(internal_site_name="CL").exists():
        PageSettings.objects.create(
            internal_site_name="CL",
            title="Find Your",
            subtitle="Club",
            tagline="A million ways to get involved, one club at a time"
        )

    if not PageSettings.objects.filter(internal_site_name="HM").exists():
        PageSettings.objects.create(
            internal_site_name="HM",
            title="Welcome To",
            subtitle="STUCO",
            tagline="Where students come together"
        )


@receiver(post_save, sender=SiteSettings)
@receiver(post_delete, sender=SiteSettings)
@receiver(post_save, sender=PageSettings)
@receiver(post_delete, sender=PageSettings)
def on_management_change(sender, instance, **kwargs):
    revalidate_frontend("management")
