#Filename: project/models.py
#Name: Marissa Kachadoorian
#Description: This file contains all the models for my project. The Project model is actually the model for a recipe and UsersRecipes is a model to connect Project and User.

from django.db import models
from django.urls import reverse
# Create your models here.


class Project(models.Model):
    """Encapsulate the idea of a recipe and its attributes. A project is a recipe that can belong to multiple users."""

    #data attributes of a recipe:
    recipe = models.TextField(blank=True)
    cook = models.TextField(blank=True)
    image = models.URLField(blank=True)
    instructions = models.TextField(blank=True)
    cooktime = models.IntegerField(default=1)

    def __repr__(self):
        """return a string representation of this object."""
        return '%s %s' % (self.cook, self.recipe)

    def get_absolute_url(self):
        """Return a URL to display this recipe."""
        return reverse("recipe", kwargs={"pk": self.pk})

    def get_all_comments(self):
        """return a QuerySet of all comments for this person."""
        
        #get all comments of this recipe and define as 'messages'
        comment = Comment.objects.filter(project=self.pk)

        #return messages
        return comment

    def __str__(self):
        """return a string representation of this object."""
        return self.recipe

    class Meta:
        abstract = True


class Recipe(Project):
    pass

class User(models.Model):
    """This class will define a user and their attributes."""
    
    #data attributes of a user
    name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    profile_image = models.URLField(blank=True)
    biography = models.TextField(blank=True)

    def __repr__(self):
        """return a string representation of this object."""

        return '%s %s' % (self.name, self.email)

    def get_absolute_url(self):
        """Return a URL to display this user."""

        return reverse("user", kwargs={"pk": self.pk})

    def get_all_statusmessages(self):
        """return a QuerySet of all quotes for this person."""
        
        #get all status of this person
        statusmessages = StatusMessage.objects.filter(user=self.pk)

        #return statusmessages
        return statusmessages

    def __str__(self):
        """return a string representation of this object."""

        return self.name

    def get_all_recipes(self):
        """return a QuerySet of all recipes for this user."""

        #get all recipes of this user
        recipes = UsersRecipes.objects.filter(user=self.pk)

        #return recipes
        return recipes


class StatusMessage(models.Model):
    """Encapsulate the idea of a status post on a user's profile."""

    #data attributes of a profile
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image =  models.URLField(blank=True)
    
    def __str__(self):
        """return a string representation of this object."""

        return '%s %s' % (self.message, self.image)


class UsersRecipes(models.Model):
    """A model to connect User and Project(recipe)."""

    #foreign key relationships and one data attribute
    timestamp = models.DateTimeField(blank=True, auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        """return a string representation of this object."""

        return '%s %s' % (self.timestamp, self.project)

class Comment(models.Model):
    """Encapsulate the idea of a comment on a recipe."""

    #data attributes of a profile and foreign key relationships to user and project
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image =  models.URLField(blank=True)
    project = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    
    def __str__(self):
        """return a string representation of this object."""

        return '%s %s' % (self.message, self.image)

# class Promise(models.Model):
#     title = models.CharField(max_length=300)
#     description = models.TextField(blank=True)
#     made_on = models.DateField()