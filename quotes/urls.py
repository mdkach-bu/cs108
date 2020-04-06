#file: quotes/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions

from django.urls import path
from .views import * #HomePageView, QuotePageView, RandomQuoteView, PersonPageView

urlpatterns = [
    path('', RandomQuoteView.as_view(), name="random"), #pick a random quote
    path('all', HomePageView.as_view(), name='all'), #generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), #show one quote
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name='update_quote'), #update
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), #show one person
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), #create new quote
    path('quote/<int:pk>/delete', DeleteQuoteView.as_view(), name='delete_quote'), #delete
    path('person/<int:pk>/add_image', add_image, name='add_image'), #add an image

]