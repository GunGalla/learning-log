"""Views of the page."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Homepage of Learning Log app."""
    return render(request, 'learning_logs/index.html')


@login_required()
def topics(request):
    """Shows topics list."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required()
def topic(request, topic_id):
    """Show dedicated topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required()
def new_topic(request):
    """Creates new topic."""
    if request.method != 'POST':
        # New empty form creation
        form = TopicForm()
    else:
        # Send data; data processing
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Show empty or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required()
def new_entry(request, topic_id):
    """Creates new entry in the topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # New empty form creation
        form = EntryForm()
    else:
        # Send data; data processing
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Show empty or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    """Edit entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Entry didn't change
        form = EntryForm(instance=entry)
    else:
        # Send data; data processing
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request, theme):
    """Check if user has access to topic."""
    if theme.owner != request.user:
        raise Http404
