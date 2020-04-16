#file: cs108/urls.py
#author: Marissa Kachadoorian (mdkach@bu.edu) (3/26/20)
#description: direct URL requests to view functions
"""cs108 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #new
from django.conf.urls.static import static 
from django.conf import settings

#project-level URL patterns
urlpatterns = [
    path('admin/', admin.site.urls), #built in django admin application
    path('pages/', include('pages.urls')), #include the URLs from our pages project's url
    path('quotes/', include('quotes.urls')), #include the URLs from our quotes project's url
    path('mini_fb/', include('mini_fb.urls')), #include the URLs from our mini_fb project's url
    path('project/', include('project.urls')), #include the URLs from my project's url
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)