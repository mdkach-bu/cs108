#file: project/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView, RecipePageView, OneRecipePageView, UserPageView, UpdateRecipeView, OneUserPageView, UpdateUserView, CreateRecipeView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), 
    path('recipe_list/', RecipePageView.as_view(), name="recipe_list"), 
    path('recipe_list/<int:pk>', OneRecipePageView.as_view(), name='recipe'), #show one recipe
    path('all_users/', UserPageView.as_view(), name="all_users"), 
    path('recipe_list/<int:pk>/update', UpdateRecipeView.as_view(), name='update_recipe'), #update
    path('all_users/<int:pk>', OneUserPageView.as_view(), name='user'),
    path('all_users/<int:pk>/update', UpdateUserView.as_view(), name='update_user'), #update
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'),
    #path('create_profile', CreateProfileView.as_view(), name='create_profile'),


]