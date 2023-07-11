from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm, SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()

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

    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def user_record(request, pk):
    if request.user.is_authenticated:

        user_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'user_record': user_record})
    else:
        messages.success(request, 'You Must Be logged In to View This Record')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.success(
            request, 'You Must Be logged In to Delete This Record')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Successfully Added')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(
            request, 'You Must Be logged In to Add This Record')
    return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Successfully Updated')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(
            request, 'You Must Be logged In to Update This Record')
    return redirect('home')
