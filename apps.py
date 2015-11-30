from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UserConfig(AppConfig):
    name = 'django-email-auth'
    verbose_name = _("Authentication")
