"""
Definition of forms.
"""

from turtle import width
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Model

class GPTForm(forms.Form):
    genre = forms.CharField(label='Genre', max_length=10, required=False)
    artist = forms.CharField(label='Artist', max_length=300, required=False)
    question = forms.CharField(label = 'Description', widget=forms.Textarea(attrs={"rows":"5", "cols":"40"}))


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
