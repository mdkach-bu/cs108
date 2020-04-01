#file: mini_fb/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='home'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), #show one person

]