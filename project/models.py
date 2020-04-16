from django.db import models
from django.urls import reverse
# Create your models here.


class Project(models.Model):
    """Encapsulate the idea of a recipe. A project is a recipe that can belong to multiple users."""

    #data attributes of a recipe:
    recipe = models.TextField(blank=True)
    cook = models.TextField(blank=True)
    image = models.URLField(blank=True)
    instructions = models.TextField(blank=True)

    def __repr__(self):
        """return a string representation of this object."""
        return '%s %s' % (self.cook, self.recipe)

    def get_absolute_url(self):
        """Return a URL to display this recipe."""
        return reverse("recipe", kwargs={"pk": self.pk})

class User(models.Model):
    """This class will define a user and their attributes."""
    
    #data attributes of a user
    name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profile_image = models.URLField(blank=True)
    biography = models.TextField(blank=True)

    def __repr__(self):
        """return a string representation of this object."""
        return '%s %s' % (self.name, self.email)

    def get_absolute_url(self):
        """Return a URL to display this user."""
        return reverse("user", kwargs={"pk": self.pk})

    # def get_all_recipes(self):
