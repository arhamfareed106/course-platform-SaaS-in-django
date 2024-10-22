from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register the User model with the default UserAdmin
admin.site.unregister(User)  # Unregister if it was registered previously
admin.site.register(User, UserAdmin)
