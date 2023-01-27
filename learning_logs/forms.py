"""Form creation module."""
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """New topic settngs."""
    class Meta:
        """Settings."""
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """New enrty settings."""
    class Meta:
        """Settings."""
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
