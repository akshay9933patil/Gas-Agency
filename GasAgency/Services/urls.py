from django.urls import path
from . import  views



urlpatterns = [

    path('service_request/', views.submit_service_request, name='service_request_url'),

    path('request_tracking/', views.request_tracking, name='request_tracking_url'),

    path('update_request/<int:request_id>/', views.update_request, name='update_request_url'),
]
