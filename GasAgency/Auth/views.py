from django.shortcuts import render, redirect
from .forms import CustomerForm, CustomerRepresentativeForm, CustomerLoginForm, CustomerRepresentativeLoginForm
from .models import CustomerRepresentative
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('login_customer_url')  
    else:
        form = CustomerForm()
    return render(request, 'Auth/register_customer.html', {'form': form})


def register_customer_representative(request):
    if request.method == 'POST':
        form = CustomerRepresentativeForm(request.POST)
        if form.is_valid():
            user = form.save()
            representative = CustomerRepresentative.objects.create_customer_representative(
                email=user.email,
                password=user.password,
            )
            return redirect('login') 
    else:
        form = CustomerRepresentativeForm()
    return render(request, 'customer_service/register_customer_representative.html', {'form': form})



def customer_login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"username-->{username},password-->{username}")
            user = authenticate(username=username, password=password)
            password = form.cleaned_data.get('password')
            if user is not None:
                login(request, user)
                # return HttpResponse('<h1> Logged in Successfully <h1>')
                return redirect('service_request_url')  # Redirect to the home page after login
            else:
                # Handle invalid credentials
                pass
    else:
        form = CustomerLoginForm()
    return render(request, 'Auth/login_customer.html', {'form': form})



def customer_representative_login_view(request):
    if request.method == 'POST':
        form = CustomerRepresentativeLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('<h1> Logged in Successfully <h1>')
                return redirect('home')  
            else:
                pass
    else:
        form = CustomerRepresentativeLoginForm()
    return render(request, 'Auth/customer_login.html', {'form': form})
