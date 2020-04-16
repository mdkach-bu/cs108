from django import forms
from .models import Project, User

class UpdateRecipeForm(forms.ModelForm):
    """A form to update a recipe to the database."""

    class Meta:
        """Associate this form with the Project mode."""
        model = Project
        fields = ['recipe', 'cook', 'instructions', 'image']

class UpdateUserForm(forms.ModelForm):
    """A form to update a recipe to the database."""

    class Meta:
        """Associate this form with the Project mode."""
        model = User
        fields = ['name', 'email', 'biography']

class CreateRecipeForm(forms.ModelForm):
    """A form to add new profiles to the database"""
    recipe = forms.CharField(label="Recipe Name", required=True)
    cook = forms.CharField(label="Cook", required=True)
    instructions = forms.CharField(label="Instructions", required=True)
    image = forms.ImageField(label="Picture", required=True)
    
    class Meta:
        model = Project
        fields = ['recipe', 'cook', 'instructions', 'image']