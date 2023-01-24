"""Views of the page."""
from django.shortcuts import render
from .models import Topic


def index(request):
    """Homepage of Learning Log app."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Shows topics list."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
