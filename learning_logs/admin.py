"""Admin module for learning_log project."""
from django.contrib import admin
from .models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
