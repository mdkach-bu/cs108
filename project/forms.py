from django import forms
from .models import Project, User, StatusMessage, Comment, UsersRecipes

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
    image = forms.URLField(label="Picture URL", required=True)
    
    class Meta:
        model = Project
        fields = ['recipe', 'cook', 'instructions', 'image']

class CreateStatusMessageForm(forms.ModelForm):
    """A form to create a status."""

    image = forms.URLField(label="Upload Picture", required=False)

    class Meta:
        model = StatusMessage 
        fields = ['message', 'image']

class CreateCommentForm(forms.ModelForm):
    """A form to create a comment."""

    image = forms.URLField(label="Upload Picture", required=False)

    class Meta:
        model = Comment 
        fields = ['message', 'image', 'user']

class CreateUserForm(forms.ModelForm):
    """A form to add new profiles to the database"""

    name = forms.CharField(label="Name", required=True)
    email = forms.CharField(label="Email Address", required=True)
    biography = forms.CharField(label="Biography", required=True)
    profile_image = forms.URLField(label="Picture URL", required=True)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'biography', 'profile_image']

class AddRecipeForm(forms.ModelForm):
    """A form to add a recipe to a cookbook."""

    
    class Meta:
        model = UsersRecipes 
        fields = ['project',]