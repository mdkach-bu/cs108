from django.shortcuts import render
from .models import Project, User, StatusMessage, Comment
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import *

class HomePageView(TemplateView):
    """create a subclass of TemplateView to display our homepage."""
    template_name = 'project/home.html'
    

class RecipePageView(ListView):
    """create a subclass of ListView to display all the recipes."""
    
    Model = Project
    template_name = 'project/recipe_list.html'
    context_object_name = 'all_project_list'
    queryset = Project.objects.all()

class OneRecipePageView(DetailView):
    """shows one recipe and all its details."""

    Model = Project
    template_name = 'project/recipe.html'
    context_object_name = 'recipe'
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(OneRecipePageView, self).get_context_data(**kwargs)
        form = CreateCommentForm()
        context['create_comment'] = form
        return context


def create_comment(request, pk):
    '''Process a form submission to post a new comment.'''

    project = Project.objects.get(pk=pk)
    form = CreateCommentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' or request.method == 'FILES':
        message = request.POST['message']
        if message:
            sm = form.save(commit=False)
            sm.project = project
            sm.save()
    #return a response, response should redirect to a URL.
    return redirect(reverse('recipe', kwargs={'pk':pk}))

class UserPageView(ListView):
    """show a list of users."""
    Model = User
    template_name = 'project/all_users.html'
    context_object_name = 'all_user_list'
    queryset = User.objects.all()
    
class UpdateRecipeView(UpdateView):
    """A view to update a quote and save it to the database."""

    form_class = UpdateRecipeForm
    template_name = 'project/update_recipe.html'
    queryset = Project.objects.all()
    

class OneUserPageView(DetailView):
    """shows one user and all its details."""

    Model = User
    template_name = 'project/user.html'
    context_object_name = 'user'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(OneUserPageView, self).get_context_data(**kwargs)
        form = CreateStatusMessageForm()
        form_2 = AddRecipeForm()
        context['add_recipe_to_cookbook'] = form_2
        context['create_status_form'] = form
        return context

def add_recipe_to_cookbook(request, pk):
    '''Process a form submission to add a recipe to a cookbook.'''

    user = User.objects.get(pk=pk)
    form = AddRecipeForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' or request.method == 'FILES':
        sm = form.save(commit=False)
        sm.user = user
        sm.save()
    #return a response, response should redirect to a URL.
    return redirect(reverse('user', kwargs={'pk':pk}))

class UpdateUserView(UpdateView):
    """A view to update a quote and save it to the database."""

    form_class = UpdateUserForm
    template_name = 'project/update_user.html'
    queryset = User.objects.all()


def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''

    user = User.objects.get(pk=pk)
    form = CreateStatusMessageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' or request.method == 'FILES':
        message = request.POST['message']
        if message:
            sm = form.save(commit=False)
            sm.user = user
            sm.message = message
            sm.save()
    #return a response, response should redirect to a URL.
    return redirect(reverse('user', kwargs={'pk':user.pk}))

class CreateRecipeView(CreateView):
    """A view to create a new quote and save it to the database."""

    form_class = CreateRecipeForm
    template_name = 'project/create_recipe_form.html'

class CreateUserView(CreateView):
    """A view to create a new quote and save it to the database."""

    form_class = CreateUserForm
    template_name = 'project/create_user_form.html'


class DeleteStatusMessageView(DeleteView):
    """A view to update a status and save it to the database."""

    template_name = 'project/delete_status_message_form.html'
    queryset = StatusMessage.objects.all()
    
    def get_object(self):
        """the objective of which is to return the StatusMessage object that should be deleted."""
        
        # read the URL data values into variables
        user_pk = self.kwargs['user_pk']
        statusmessage_pk = self.kwargs['statusmessage_pk']

        return StatusMessage.objects.get(pk=statusmessage_pk)

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""
        
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        st_msg = StatusMessage.objects.get(pk=self.kwargs['statusmessage_pk'])

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
        return reverse('user', kwargs={'pk':user.pk})