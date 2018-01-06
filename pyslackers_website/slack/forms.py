from django import forms

from .validators import validate_is_not_burner_domain


class SlackInviteForm(forms.Form):
    """Form for slack invitation requests"""
    email = forms.EmailField(validators=[
        validate_is_not_burner_domain,
    ])
    accept_tos = forms.BooleanField()
