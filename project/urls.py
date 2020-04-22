#file: project/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), 
    path('recipe_list/', RecipePageView.as_view(), name="recipe_list"), 
    path('recipe_list/<int:pk>', OneRecipePageView.as_view(), name='recipe'), #show one recipe
    path('all_users/', UserPageView.as_view(), name="all_users"), 
    path('recipe_list/<int:pk>/update', UpdateRecipeView.as_view(), name='update_recipe'), #update
    path('all_users/<int:pk>', OneUserPageView.as_view(), name='user'),
    path('all_users/<int:pk>/update', UpdateUserView.as_view(), name='update_user'), #update
    path('create_recipe', CreateRecipeView.as_view(), name='create_recipe'),
    path('all_users/<int:pk>/post_status', create_status_message, name='post_status'),
    path('recipe_list/<int:pk>/post_comment', create_comment, name='post_comment'),
    path('create_user', CreateUserView.as_view(), name='create_user'),
    path('all_users/<int:pk>/add_recipe', add_recipe_to_cookbook, name='add_recipe'),
    path('all_users/<int:user_pk>/delete_status/<int:statusmessage_pk>', DeleteStatusMessageView.as_view(), name='delete_status'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)