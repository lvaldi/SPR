from django.shortcuts import render
from django.http import HttpResponse
# from django.views import View

# Create your views here.
# class sign_in_view(View):
    # def get(request, self, *args, **kwargs):
    #     template_name = 'login.html'
    #     print(args, kwargs)
    #     return render(request, self.template_name, {})

def sign_in_view(request, *args, **kwargs):
    template_name = 'login.html'
    print(args, kwargs)
    return render(request, template_name, {})
