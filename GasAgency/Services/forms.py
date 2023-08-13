from django import forms
from .models import ServiceRequest, RequestUpdate


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'request_details', 'file_attachment']
        

class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = RequestUpdate
        fields = ['update_details']
