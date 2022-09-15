from django.forms import ModelForm
from .models import User
from django import forms
from django.forms import CharField, Form, PasswordInput
from django.utils.translation import gettext_lazy as _


# class RegisterForm(forms.ModelForm):
#     # fullname = forms.CharField(max_length=100)
#     # email = forms.EmailField()
#     # password = forms.CharField(widget=PasswordInput)
#     # mobile = forms.CharField()
#     # address = forms.CharField()
#     username= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"Username"}))
#     class Meta:
#         model = User
#         fields = ["fullname","username","email", "password","mobile","address",]
#         exclude = ["DOB","gender","field_type","User_type","assigned_client"]


# class LoginForm(forms.ModelForm):
#     # username= forms.CharField(max_length=100,widget= forms.TextInput
#     #                        (attrs={'class':'input--style-3','placeholder':"Username"}))
#     email= forms.CharField(max_length=100,widget= forms.TextInput
#                            (attrs={'class':'input--style-3','placeholder':"Email"}))
#     password= forms.CharField(max_length=100,widget= forms.PasswordInput
#                            (attrs={'class':'input--style-3','placeholder':"Password"}))
#     class Meta:
#         model = User
#         fields = ["email", "password",]

STATE_CHOICE2=((
    ('TL','TL'),
    ('Tranni','Tranni'),

))

class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label=_("Username"), max_length=30)
    first_name = forms.CharField(label=_("First name"), max_length=30)
    last_name = forms.CharField(label=_("Last name"), max_length=30)
    mobile_number = forms.CharField(label=_("Mobile number"), max_length=30)
    email = forms.CharField(label=_("Email"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    User_type = forms.ChoiceField(choices = STATE_CHOICE2, 
                              initial='', widget=forms.Select(), required=True)
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "mobile_number",
            "email",
            "password",
            "User_type",
        )