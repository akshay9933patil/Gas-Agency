from django.contrib import admin
from .models import ServiceRequest, RequestUpdate

admin.site.register(ServiceRequest)
admin.site.register(RequestUpdate)
