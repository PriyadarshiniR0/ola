from ride.views import *
from django.urls import path
app_name='ola'
urlpatterns=[
    path('auto/',auto,name='auto'),
    path('cab/',cab,name='cab')
]