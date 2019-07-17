from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class sign_in_view(View):
    def get(self, request, *args, **kwargs):
        template_name = 'login.html'
        print(args, kwargs)
        return render(request, template_name, {})
