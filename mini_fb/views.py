from django.shortcuts import render

# Create your views here.
from .models import Profile, StatusMessage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
class ShowAllProfilesView(ListView):
    """Create a subclass of ListView to display all profiles."""

    model = Profile #retrieve objects of type Profile from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list' #how to find the data in the template file


class ShowProfilePageView(DetailView):
    """create a subclass of DetailView to show the profile of one person."""

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    """A view to create a new quote and save it to the database."""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):
    """A view to update a quote and save it to the database."""

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()

def create_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''
    profile = Profile.objects.get(pk=pk)

    form = CreateStatusMessageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' or request.method == 'FILES':

        message = request.POST['message']
        #image = request.POST['image']

        # save the new status message object to the database
        if message:

            sm = form.save(commit=False)
            sm.profile = profile
            sm.message = message
            sm.save()
            
    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))
    

class DeleteStatusMessageView(DeleteView):
    """A view to update a quote and save it to the database."""

    template_name = 'mini_fb/delete_status_form.html'
    queryset = StatusMessage.objects.all()
    
    def get_object(self):
        """the objective of which is to return the StatusMessage object that should be deleted."""
        
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        return StatusMessage.objects.get(pk=status_pk)

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""
        #get the default context data:
        #this will include the Person record for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        context['st_msg'] = st_msg

        #return the context dictionary
        return context

    def get_success_url(self):
        """Return a URL to which we should be directed after the delete."""
        
        # get the pk for this quote
        pk = self.kwargs.get('status_pk')
        status_message = StatusMessage.objects.filter(pk=pk).first()
        
        #find the person associated with the quote
        profile = status_message.profile
        return reverse('show_profile_page', kwargs={'pk':profile.pk})
        
class ShowNewsFeedView(DetailView):
    """"A view to display a newsfeed and save it to the database."""

    model = Profile
    template_name = 'mini_fb/show_news_feed.html'
    context_object_name = 'profile'
    queryset = Profile.objects.all()
    

class ShowPossibleFriendsView(DetailView):
    """A view to display friend suggestions and save it to the database."""
    
    model = Profile
    template_name = 'mini_fb/show_possible_friends.html'
    context_object_name = 'profile'
    queryset = Profile.objects.all()

def add_friend(request, profile_pk, friend_pk):
    """The objective of this function is to process the add_friend request and to add a friend for a given profile."""

    #find the Profile object which is adding the friend and store it into a variable
    person_to_add_friend = Profile.objects.get(pk=profile_pk)
    #find the Profile object of the friend to add, and store it into another variable
    added_friend = Profile.objects.get(pk=friend_pk)
    #add that friend's Profile into the profile.friends object (using the method add)
    person_to_add_friend.friends.add(added_friend)
    #save the profile object
    added_friend.save()
    return redirect(reverse('show_profile_page', kwargs={'pk':profile_pk}))
