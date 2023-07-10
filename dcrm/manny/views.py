from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        pasword = request.POST['password']

        # Authicate
        user = authenticate(request, username=username, password=pasword)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error. Please try again")
            return redirect('home')

    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You've been logfed out")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})