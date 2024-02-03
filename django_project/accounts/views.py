from django.contrib.auth.forms import UserCreationForm
from django.views import generic

    

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a login page, for example
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})