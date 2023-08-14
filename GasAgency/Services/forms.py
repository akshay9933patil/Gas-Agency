from django import forms
from .models import ServiceRequest, RequestUpdate


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'request_details', 'file_attachment']
        

class RequestUpdateForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    update_details = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = RequestUpdate
        fields = ['status','update_details']
