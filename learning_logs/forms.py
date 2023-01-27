"""Form creation module."""
from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    """New topic settngs."""
    class Meta:
        """Settings."""
        model = Topic
        fields = ['text']
        labels = {'text': ''}
