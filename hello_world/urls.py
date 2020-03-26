#file: hello_world/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView, name='home'),

]