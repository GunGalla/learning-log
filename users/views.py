"""Views of user's page."""
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Shows empty form
        form = UserCreationForm()
    else:
        # Filled form processing
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login and redirect to homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    # Show empty or invalid form
    context = {'form': form}
    return render(request, 'users/register.html', context)
