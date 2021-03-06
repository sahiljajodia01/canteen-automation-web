from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User

# Our custom user model.
admin.site.register(User, UserAdmin)

# Remove groups from admin site.
admin.site.unregister(Group)
