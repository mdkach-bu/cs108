#file: project/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (4/26/20)
#description: direct URL requests to view functions such as the homepage, recipe list, one recipe, 
# all profiles in a list, update a recipe, show one user, update a profile, create a new recipe, create 
#a status message post, post a comment on a recipe, create a new profile, and create a new recipe.

from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), #show homepage
    path('recipe_list/', RecipePageView.as_view(), name="recipe_list"), #show recipe list
    path('recipe_list/<int:pk>', OneRecipePageView.as_view(), name='recipe'), #show one recipe
    path('all_users/', UserPageView.as_view(), name="all_users"), #show all profiles
    path('recipe_list/<int:pk>/update', UpdateRecipeView.as_view(), name='update_recipe'), #update recipe
    path('all_users/<int:pk>', OneUserPageView.as_view(), name='user'), #show one user
    path('all_users/<int:pk>/update', UpdateUserView.as_view(), name='update_user'), #update profile
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'), #create recipe
    path('all_users/<int:pk>/post_status', create_status_message, name='post_status'), #create status message
    path('recipe_list/<int:pk>/post_comment', create_comment, name='post_comment'), #post comment
    path('create_user', CreateUserView.as_view(), name='create_user'), #create new profile
    path('all_users/<int:pk>/add_recipe', add_recipe_to_cookbook, name='add_recipe'), #create new recipe
    path('all_users/<int:user_pk>/delete_status/<int:statusmessage_pk>', DeleteStatusMessageView.as_view(), name='delete_status'), #delete status message

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)