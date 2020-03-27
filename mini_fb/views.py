from django.shortcuts import render

# Create your views here.
from .models import Profile
from django.views.generic import ListView

class ShowAllProfilesView(ListView):
    """Create a subclass of ListView to display all quotes."""

    model = Profile #retrieve objects of type Profile from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list' #how to find the data in the template file
