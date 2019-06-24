from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sign_in_view(request, *args, **kwargs):
    template_name = 'login.html'
    print(args, kwargs)
    return render(request, template_name, {})


# class patient_login_view(View):
# 	template_name = "Patient/login.html"
# 	def get(self, request, *args, **kwargs):
# 		if request.GET.get('pid', ''):
# 			return HttpResponseRedirect('%s/detail/' % request.GET.get('pid', ''))
# 		return render(request, self.template_name, context)
