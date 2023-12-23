from django import forms
from .models import Subscriber
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "birth_date", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    pass