from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class loginView(View):
    template_name="user/login.html"

    def get(self, request):
        return render(request,self.template_name)

class registerView(View):
    template_name="user/register.html"

    def get(self, request):
        return render(request, self.template_name)