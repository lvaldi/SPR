from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sign_in_view(request, *args, **kwargs):
    template_name = 'login.html'
    print(args, kwargs)
    return render(request, template_name, {})
