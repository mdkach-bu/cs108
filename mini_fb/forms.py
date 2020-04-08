from django import forms
from .models import Profile, StatusMessage 


class CreateProfileForm(forms.ModelForm):
    """A form to add new profiles to the database"""
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email Address", required=True)
    image_url = forms.CharField(label="Profile Picture", required=True)
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'image_url',]

class UpdateProfileForm(forms.ModelForm):
    """A form to update a quote to the database."""
    
    class Meta:
        model = Profile
        fields = ['city', 'email_address', 'image_url',]

class CreateStatusMessageForm(forms.ModelForm):
    """A form to update a status."""

    image = forms.ImageField(label="Upload Image", required=False)

    class Meta:
        model = StatusMessage 
        fields = ['message', 'image']

