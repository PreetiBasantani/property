from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:

        model=User
        fields=('username','first_name','last_name','email','password')


class Password2Form(UserForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserForm.Meta):
        fields=UserForm.Meta.fields + ('password2',)