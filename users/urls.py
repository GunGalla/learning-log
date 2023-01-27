"""URL scheme for users."""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Default auth URL
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]
