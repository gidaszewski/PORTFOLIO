from django.urls import path
from Home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('resume', resume, name='resume'),
    path('projects', projects, name='projects'),
    path('email-success', mail_success, name="email-success")
]