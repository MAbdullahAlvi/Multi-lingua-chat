from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()



class MessageForm(forms.Form):
    LANG_CHOICES = [
        ('English', 'English'),
        ('Urdu', 'Urdu'),
        ('Chinese (Simplified)', 'Chinese (Simplified)'),
        ('Chinese (Traditional)', 'Chinese (Traditional)'),
    ]
    message = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANG_CHOICES)
