#Filename: project/views.py
#Name: Marissa Kachadoorian (mdkach@bu.edu)
#Description: This file contains all the views for my project deriving from TemplateView, DetailView, UpdateView, CreateView, and DeleteView

from django.shortcuts import render
from .models import Project, User, StatusMessage, Comment
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import *

class HomePageView(TemplateView):
    """create a subclass of TemplateView to display our homepage."""

    template_name = 'project/home.html' #define template
    

class RecipePageView(ListView):
    """create a subclass of ListView to display all the recipes."""
    
    Model = Recipe #retrieve objects of type Project from the database

    template_name = 'project/recipe_list.html' #define template

    context_object_name = 'all_project_list' #how to find the data in the template file

    queryset = Recipe.objects.all()

class OneRecipePageView(DetailView):
    """shows one recipe and all its details."""

    Model = Recipe #retrieve objects of type Project from the database

    template_name = 'project/recipe.html'

    context_object_name = 'recipe' #how to find the data in the template file

    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        #get the default context data:
        #this will include the User record for this page view

        context = super(OneRecipePageView, self).get_context_data(**kwargs)

        #create create comment form
        form = CreateCommentForm()

        context['create_comment'] = form

        #return context dictionary
        return context


def create_comment(request, pk):
    '''Process a form submission to post a new comment.'''

    #find the project for whom we are submitting the comment
    project = Recipe.objects.get(pk=pk)

    #read request data into CreateCommentForm object
    form = CreateCommentForm(request.POST or None, request.FILES or None)

    #if request method = post or files, proceed
    if request.method == 'POST' or request.method == 'FILES':

        message = request.POST['message']

        if message:

            sm = form.save(commit=False) #create sm form but do not save

            sm.project = project 

            sm.save() #save

    #return a response, response should redirect to a URL.
    return redirect(reverse('recipe', kwargs={'pk':pk}))

class UserPageView(ListView):
    """A view to show a list of users."""

    Model = User #retrieve objects of type User from the database

    template_name = 'project/all_users.html'

    context_object_name = 'all_user_list' #how to find the data in the template file

    queryset = User.objects.all()
    
class UpdateRecipeView(UpdateView):
    """A view to update a recipe and save it to the database."""

    form_class = UpdateRecipeForm #define form class

    template_name = 'project/update_recipe.html'

    queryset = Recipe.objects.all()
    
    # def update_view(request):
    #     if request.method == 'POST':
    #         form = DietaryForm(request.POST)
    #         if form.is_valid():
    #             Diets = form.cleaned_data.get('Diets')
    #             # do something with your results
    #     else:
    #         form = DietaryForm

    #     return render_to_response('update_recipe.html', {'form': form}, context_instance=RequestContext(request))

class OneUserPageView(DetailView):
    """A view to show one user and all its details."""

    Model = User #retrieve objects of type User from the database

    template_name = 'project/user.html'

    context_object_name = 'user' #how to find the data in the template file

    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        #get the default context data:
        #this will include the User record for this page view

        context = super(OneUserPageView, self).get_context_data(**kwargs)

        #create createstatus form
        form = CreateStatusMessageForm()

        form_2 = AddRecipeForm()

        #create context dictionary 
        context['add_recipe_to_cookbook'] = form_2

        context['create_status_form'] = form

        #return context dictionary
        return context

def add_recipe_to_cookbook(request, pk):
    '''Process a form submission to add a recipe to a cookbook.'''

    #find the user for whom we are submitting the status message
    user = User.objects.get(pk=pk)

    #read request data into AddRecipeForm object
    form = AddRecipeForm(request.POST or None, request.FILES or None)

    #if request is post or files, proceed
    if request.method == 'POST' or request.method == 'FILES':

        sm = form.save(commit=False) #create sm form object but do not save

        sm.user = user

        sm.save() #save

    #return a response, response should redirect to a URL.
    return redirect(reverse('user', kwargs={'pk':pk}))

class UpdateUserView(UpdateView):
    """A view to update a profile and save it to the database."""

    form_class = UpdateUserForm

    template_name = 'project/update_user.html'

    queryset = User.objects.all()


def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''

    #find the user for whom we are submitting the status message
    user = User.objects.get(pk=pk)

    #read request data into CreateStatusMessageForm object
    form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

    #if request is post or files, proceed
    if request.method == 'POST' or request.method == 'FILES':

        message = request.POST['message']

        #if request is post or files, and if message, proceed
        if message:

            sm = form.save(commit=False) #create sm form object but do not save
            sm.user = user
            sm.message = message
            sm.save() #save

    #return a response, response should redirect to a URL.
    return redirect(reverse('user', kwargs={'pk':user.pk}))

class CreateRecipeView(CreateView):
    """A view to create a new recipe and save it to the database."""

    form_class = CreateRecipeForm

    template_name = 'project/create_recipe_form.html' #define template

class CreateUserView(CreateView):
    """A view to create a new user and save it to the database."""

    form_class = CreateUserForm

    template_name = 'project/create_user_form.html' #define template


class DeleteStatusMessageView(DeleteView):
    """A view to delete a status and save it to the database."""

    template_name = 'project/delete_status_message_form.html' #define template

    queryset = StatusMessage.objects.all()
    
    def get_object(self):
        """the objective of which is to return the StatusMessage object that should be deleted."""
        
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']

        statusmessage_pk = self.kwargs['statusmessage_pk']

        return StatusMessage.objects.get(pk=statusmessage_pk)

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""

        #get the default context data:

        #this will include the StatusMessage record for this page view

        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        st_msg = StatusMessage.objects.get(pk=self.kwargs['statusmessage_pk'])

        #create dictionary:
        context['st_msg'] = st_msg

        #return the context dictionary
        return context

    def get_success_url(self):
        """Return a URL to which we should be directed after the delete."""
        
        # get the pk for this quote

        pk = self.kwargs.get('statusmessage_pk')

        status_message = StatusMessage.objects.filter(pk=pk).first()
        
        #find the person associated with the quote

        user = status_message.user

        #reverse to show the profile page

        return reverse('user', kwargs={'pk':user.pk})