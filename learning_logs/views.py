"""Views of the page."""
from django.shortcuts import render


def index(request):
    """Homepage of Learning Log app."""
    return render(request, 'learning_logs/index.html')
