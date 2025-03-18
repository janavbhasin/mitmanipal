# registration/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            # Redirect to success page with user data as query parameters
            return redirect(f"/success/?username={username}&email={email}&contact={contact}")
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

def success(request):
    # Retrieve user data from query parameters
    username = request.GET.get('username')
    email = request.GET.get('email')
    contact = request.GET.get('contact')
    
    # Render the success page with user details
    return render(request, 'registration/success.html', {'username': username, 'email': email, 'contact': contact})
