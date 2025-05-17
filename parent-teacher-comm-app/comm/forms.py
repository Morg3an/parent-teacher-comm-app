from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Message, Meeting

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")

class LoginForm(AuthenticationForm):
    pass

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["recipient", "body"]

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["student", "scheduled_for", "notes"]
        widgets = {
            "scheduled_for": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }