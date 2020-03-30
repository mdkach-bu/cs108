#file: quotes/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import * #HomePageView, QuotePageView, RandomQuoteView, PersonPageView

urlpatterns = [
    path('', RandomQuoteView.as_view(), name="random"), #pick a random quote
    path('all', HomePageView.as_view(), name='home'), #generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), #show one quote
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), #show one person

]