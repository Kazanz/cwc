from django import forms

from codewithchrist.models import SignUpData, Course


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpData
