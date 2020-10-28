from django.contrib import admin

# Register your models here.
from profile_todo.models import Profile, Todo

admin.site.register(Profile)
admin.site.register(Todo)
