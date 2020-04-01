from django.db import models

# Create your models here.

class Profile(models.Model):
    """Encapsulate the idea of a FB profile."""

    #data attributes of a profile:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """return a string representation of this object."""
        return '%s %s %s' % (self.first_name, self.last_name, self.city)

    def get_all_statusmessages(self):
        """return a QuerySet of all quotes for this person."""
        
        #get all status of this person
        messages = StatusMessage.objects.filter(profile=self.pk)
        return messages

class StatusMessage(models.Model):
    """Encapsulate the idea of a status post."""

    #data attributes of a profile
    timestamp = models.TextField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete="CASCADE")

    def __str__(self):
        """return a string representation of this object."""
        return self.timestamp

