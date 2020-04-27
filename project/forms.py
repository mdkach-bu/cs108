#Filename: project/forms.py
#Name: Marissa Kachadoorian (mdkach@bu.edu)
#Description: creates the class forms to update recipes, update user's profiles, create new recipes
#create a status message, create a comment on a recipe, make a new user, and add a new recipe to someone's 
#cookbook  on their personal page.

from django import forms
from .models import Project, User, StatusMessage, Comment, UsersRecipes, Recipe
from django.forms import ModelForm

class UpdateRecipeForm(forms.ModelForm):
    """A form to update a recipe to the database."""

    class Meta:
        """Associate this form with the Project mode."""

        model = Recipe #define which model to use

        fields = ['recipe', 'cook', 'instructions', 'image', 'cooktime'] #which fields from model should we use

class UpdateUserForm(forms.ModelForm):
    """A form to update a recipe to the database."""

    class Meta:
        """Associate this form with the Project mode."""

        model = User #define which model to use

        fields = ['name', 'email', 'biography'] #which fields from model should we use

class CreateRecipeForm(forms.ModelForm):
    """A form to add new profiles to the database"""

    recipe = forms.CharField(label="Recipe Name", required=True)
    cook = forms.CharField(label="Cook", required=True)
    instructions = forms.CharField(widget= forms.Textarea, label="Instructions", required=True)
    image = forms.URLField(label="Picture URL", required=True)
    cooktime = forms.IntegerField(label="Cooktime (min)", required=True)
    
    class Meta:
        """Associate this form with the Project mode."""

        model = Recipe #define which model to use

        fields = ['recipe', 'cook', 'instructions', 'image', 'cooktime'] #which fields from model should we use

class CreateStatusMessageForm(forms.ModelForm):
    """A form to create a status."""

    image = forms.ImageField(label="Upload Picture", required=False)

    class Meta:
        """Associate this form with the Project mode."""

        model = StatusMessage #define which model to use

        fields = ['message', 'image'] #which fields from model should we use

class CreateCommentForm(forms.ModelForm):
    """A form to create a comment."""

    #image = forms.URLField(label="Upload Picture", required=False)

    class Meta:
        """Associate this form with the Project mode."""

        model = Comment #define which model to use

        fields = ['message', 'user'] #which fields from model should we use

class CreateUserForm(forms.ModelForm):
    """A form to add new profiles to the database"""

    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="Email Address", required=True)
    biography = forms.CharField(widget= forms.Textarea, label="Biography", required=True)
    profile_image = forms.URLField(label="Picture URL", required=True)
    
    class Meta:
        """Associate this form with the Project mode."""

        model = User #define which model to use

        fields = ['name', 'email', 'biography', 'profile_image'] #which fields from model should we use

class AddRecipeForm(forms.ModelForm):
    """A form to add a recipe to a cookbook."""

    
    class Meta:
        """Associate this form with the Project mode."""

        model = UsersRecipes #define which model to use

        fields = ['project',] #which fields from model should we use
