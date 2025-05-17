from django.contrib import admin
from .models import User, Student, Message, Meeting
admin.site.register((User, Student, Message, Meeting))