from django.forms import ModelForm
from .models import User,Traning,Assignment
from django import forms
from django.forms import CharField, Form, PasswordInput
from django.utils.translation import gettext_lazy as _
from datetime import date


Date_format=['%Y-%m-%d', 
            '%m/%d/%Y',      
            '%m/%d/%y']

STATE_CHOICE2=((
    ('TL','TL'),
    ('Tranni','Tranni'),

))

STATE_CHOICE3=((
    ('InProcess','InProcess'),
    ('Complete','Complete'),

))

STATE_CHOICE=((
    ('Python','Python'),
    ('Java','Java'),
    ('React','React'),
    ('Angular','Angular'),
    ('Node','Node'),
    ('PHP','PHP'),

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

class TraningForm(forms.ModelForm):
    status = forms.ChoiceField(choices = STATE_CHOICE3, 
                              initial='', widget=forms.Select(), required=True)
    traning_topic = forms.ChoiceField(choices = STATE_CHOICE, 
                              initial='', widget=forms.Select(), required=True)
    # Start_traning_date = forms.DateField('%m/%d/%Y')
    # End_traning_date = forms.DateField('%m/%d/%Y')                        
    # sale_date = forms.DateField(widget=forms.DateInput(format='%d%m%Y'),input_formats=['%d%m%Y'])
    # Start_traning_date= forms.DateField(widget= forms.TextInput
    #                        (attrs={'class':"input--style-3 js-datepicker",'placeholder':"Start_traning_date"}))
    # End_traning_date= forms.DateField(widget= forms.TextInput
    #                        (attrs={'class':"input--style-3 js-datepicker",'placeholder':"End_traning_date"}))                        

    Start_traning_date = forms.DateField(input_formats=Date_format)
    End_traning_date = forms.DateField(input_formats=Date_format)

 # Perhaps you should consider a separator in this format i.e. `%d-%m-%Y` instead of `%d%m%Y`

    def __init__(self, user, *args, **kwargs):
        super(TraningForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["user"].queryset = user
        
            

    class Meta:
        model = Traning
        fields = (
            "user",
            "status",
            "Start_traning_date",
            "End_traning_date",
            "discription",
            "traning_topic",
        )        
        

class AssignmentForm(forms.ModelForm):
    user = forms.CharField(label=_("Username"), max_length=30)
    status = forms.ChoiceField(choices = STATE_CHOICE3, 
                              initial='', widget=forms.Select(), required=True)
    Start_traning_date = forms.DateField(input_formats=Date_format)
    End_traning_date = forms.DateField(input_formats=Date_format)                       

    class Meta:
        model = Assignment
        fields = (
            "user",
            "status",
            "Start_traning_date",
            "End_traning_date",
            "Topic_of_assignment",
        )

