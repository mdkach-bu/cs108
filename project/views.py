from django.shortcuts import render
from .models import Project, User, StatusMessage
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import UpdateRecipeForm, UpdateUserForm, CreateRecipeForm, CreateStatusMessageForm


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
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        return context

def create_comment(request, pk):
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
        return redirect(reverse('recipe', kwargs={'pk':user.pk}))

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
    """shows one recipe and all its details."""

    Model = User
    template_name = 'project/user.html'
    context_object_name = 'user'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(OneUserPageView, self).get_context_data(**kwargs)
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        return context

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