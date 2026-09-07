import logging
import requests
from django.conf import settings

def revalidate_frontend(tag: str) -> None:
    """
    POST to the Next.js revalidation route handler so it drops its
    cached data for the given cacheTag(...) immediately, instead of
    waiting for cacheLife('minutes') to expire naturally.
 
    Fails silently (logged) so a frontend outage never blocks an
    admin save.
    """

    logger = logging.getLogger(__name__)
 
    url = getattr(settings, "FRONTEND_REVALIDATE_URL", None)
    secret = getattr(settings, "REVALIDATE_SECRET", None)
 
    if not url or not secret:
        logger.warning(
            "Skipping frontend revalidation for tag=%r: ",
            "FRONTEND_REVALIDATE_URL / REVALIDATE_SECRET not configured",
            tag
        )
        return
 
    try:
        response = requests.post(
            url,
            json={"tag": tag},
            headers={"x-revalidate-secret": secret},
            timeout=5
        )
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to revalidate frontend tag=%r", tag)
 