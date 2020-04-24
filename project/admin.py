from django.contrib import admin
from .models import Recipe
admin.site.register(Recipe)
# Register your models here.
from .models import User, StatusMessage, UsersRecipes, Comment #Promise
admin.site.register(User)
admin.site.register(StatusMessage)
admin.site.register(UsersRecipes)
admin.site.register(Comment)
# admin.site.register(Promise)

