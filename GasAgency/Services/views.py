from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, RequestUpdate
from .forms import ServiceRequestForm, RequestUpdateForm
from Auth.models import *

@login_required(login_url="/auth/login_customer/")
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)

            # Check if the user is a Customer or CustomerRepresentative
            if isinstance(request.user, Customer):
                service_request.customer = request.user
            elif isinstance(request.user, CustomerRepresentative):

                pass


            service_request.save()
            return redirect('request_tracking_url')
    else:
        form = ServiceRequestForm()
    return render(request, 'Services/submit_service_request.html', {'form': form})


@login_required(login_url="/auth/login_customer/")
def request_tracking(request):
    if request.user.is_staff:
        # If the user is a customer representative (staff), show all requests
        all_service_requests = ServiceRequest.objects.all()
        return render(request, 'Services/request_tracking.html', {'service_requests': all_service_requests, 'is_customer_representative': True})
    else:
        # If the user is a customer, show only their requests
        user_service_requests = ServiceRequest.objects.filter(customer=request.user)
        return render(request, 'Services/request_tracking.html', {'service_requests': user_service_requests, 'is_customer_representative': False})


@login_required(login_url="/auth/login_customer/")
def update_request(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    if request.method == 'POST':
        form = RequestUpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.service_request = service_request
            update.save()
            service_request.status = form.cleaned_data['status']
            service_request.save()
            return redirect('request_tracking_url')  # Redirect to request tracking page
    else:
        form = RequestUpdateForm()
    return render(request, 'Services/update_request.html', {'form': form, 'service_request': service_request})


def home_view(request):
    return render(request, 'home.html')
