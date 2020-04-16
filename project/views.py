from django.shortcuts import render
from .models import Project, User
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from .forms import UpdateRecipeForm, UpdateUserForm, CreateRecipeForm
# Create your views here.

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

class UpdateUserView(UpdateView):
    """A view to update a quote and save it to the database."""

    form_class = UpdateUserForm
    template_name = 'project/update_user.html'
    queryset = User.objects.all()


class CreateRecipeView(CreateView):
    """A view to create a new quote and save it to the database."""

    form_class = CreateRecipeForm
    template_name = 'project/create_recipe_form.html'