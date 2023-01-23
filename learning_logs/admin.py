"""Admin module for learning_log project."""
from django.contrib import admin
from .models import Topic

admin.site.register(Topic)
