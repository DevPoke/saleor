"""
Pokestudio custom settings module.

Write here any settings customization to avoid merge conflicts with main file
saleor.settings.py
"""

from sentry_sdk.integrations.redis import RedisIntegration

from .settings import *

SILENCED_SYSTEM_CHECKS = [
    # TODO when sure, silence the commented warnings
    # Handled by traefik proxy
    'security.W002',
    # 'security.W003',
    'security.W004',
    # 'security.W008',
]


def parse_admins(text: str) -> tuple:
    """
    ADMINS format example:

    ADMINS=Admin,admin@pokestudio.it;Pokestudio,dev@pokestudio.it
    """
    if not text:
        return tuple()

    return tuple(
        tuple(item.strip().split(",")) for item in text.split(";")
    )


ADMINS = parse_admins(os.environ.get("ADMINS", None))
MANAGERS = ADMINS

INSTALLED_APPS += [
    # Insert here any custom apps
]


AUTH_PASSWORD_VALIDATORS += [
    # Insert here any custom password validator based on customer requests
]

# Add RedisIntegration to Sentry integrations if not already done.
if RedisIntegration.__name__ not in [
    i.__class__.__name__ for i in SENTRY_OPTS["integrations"]
]:
    SENTRY_OPTS["integrations"].append(RedisIntegration())
