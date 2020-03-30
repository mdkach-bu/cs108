#file: quotes/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuoteView

urlpatterns = [
    path('', RandomQuoteView.as_view(), name="random"), #pick a random quote
    path('all', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'),

]