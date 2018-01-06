from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from pyslackers_website.marketing.models import BurnerDomain


def validate_is_not_burner_domain(email: str) -> None:
    """Validate that the provided value is not from a
    suspected burner domain."""
    if BurnerDomain.is_burner(email):
        raise ValidationError(_('%(email)s is a suspected burner domain'),
                              params={'email': email})
