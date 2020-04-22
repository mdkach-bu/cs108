from django.contrib import admin
from .models import Project
admin.site.register(Project)
# Register your models here.
from .models import User, StatusMessage, UsersRecipes, Comment
admin.site.register(User)
admin.site.register(StatusMessage)
admin.site.register(UsersRecipes)
admin.site.register(Comment)

