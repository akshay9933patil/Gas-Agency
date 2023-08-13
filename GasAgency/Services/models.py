from django.db import models
from Auth.models import Customer


class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Gas Leak Repair', 'Gas Leak Repair'),
        ('Meter Installation', 'Meter Installation'),
        ('Billing Inquiry', 'Billing Inquiry'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='servicerequest')
    service_type = models.CharField(choices=SERVICE_TYPES, max_length=50)
    request_details = models.TextField()
    file_attachment = models.FileField(upload_to='service_request_attachments/', null=True, blank=True)
    submission_timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Service Request #{self.pk}"
    

class RequestUpdate(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    update_details = models.TextField()
    update_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.service_request}"
