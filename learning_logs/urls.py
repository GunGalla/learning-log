"""URL scheme for learning_logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Some dedicated topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
