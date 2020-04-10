from django.db import models
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    """Encapsulate the idea of a FB profile."""

    #data attributes of a profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        """return a string representation of this object."""
        return '%s %s' % (self.first_name, self.last_name)

    def get_all_statusmessages(self):
        """return a QuerySet of all quotes for this person."""
        
        #get all status of this person
        messages = StatusMessage.objects.filter(profile=self.pk)
        return messages

    def get_absolute_url(self):
        """Return a URL to display this quote."""
        return reverse("show_profile_page", kwargs={"pk": self.pk})

    def get_friends(self):
        """return a QuerySet of all friends for this Profile."""

        #return a QuerySet
        person = Profile.objects.filter(id=self.pk)[0]
        friends = person.friends.all()
        return friends

    def get_news_feed(self):
        """return a QuerySet of all statuses for this Profile."""
        friends = self.get_friends()
        news = StatusMessage.objects.filter(profile__in = friends).order_by("-timestamp")
        own = StatusMessage.objects.filter(profile=self.pk)
        news_page = news | own
        return news_page
   
class StatusMessage(models.Model):
    """Encapsulate the idea of a status post."""

    #data attributes of a profile
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image =  models.ImageField(blank=True)

    def __str__(self):
        """return a string representation of this object."""
        return '%s %s %s' % (self.timestamp, self.message, self.image)

