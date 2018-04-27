import os
from django.conf.urls import url

def django_view(request):
    os.execv(request.body)

urlpatterns = [
    url(r'index', django_view)
]
