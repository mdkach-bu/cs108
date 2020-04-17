from django.contrib import admin
from .models import Project
admin.site.register(Project)
# Register your models here.
from .models import User, StatusMessage
admin.site.register(User)
admin.site.register(StatusMessage)
