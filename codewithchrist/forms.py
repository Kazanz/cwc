from django import forms

from codewithchrist.models import SignUpData


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpData
