from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from .forms import *

# Create your views here.
class loginView(View):
    template_name="user/login.html"

    def get(self, request):
        return render(request,self.template_name)

class registerView(View):
    template_name="user/register.html"

    def get(self, request):
        return render(request, self.template_name)

class userListView(View):
    template_name = "user/userList.html"

    def get(self, request):
        user = User.objects.all()
        return render(request, self.template_name, {'user': user})

class requestDonorView(View):
    template_name = "user/requestDonor.html"

    def get(self, request, user):
        formRequestDonor = DonorForm()
        return render(request, self.template_name, {'user': user})
    
    def post(self, request, user):
        donor = DonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = RequestDonor(address=address, donorBloodType=donorBloodType,
                                isApproved=isApproved, username=username)
        
        donorReq.save()

        return render(request, self.template_name,{'user': user})

class requestOrganizerView(View):
    template_name = "user/requestOrganizer.html"

    def get(self, request, user):
        formRequestOrganizer = OrganizerForm()
        return render(request, self.template_name, {'user': user})
    
    def post(self, request, user):
        organizer = OrganizerForm(request.POST)

        hospitalName = request.POST.get('hospitalName')
        hospitalAddress = request.POST.get('hospitalAddress')
        businessEmail = request.POST.get('businessEmail')
        contactInfo = request.POST.get('contactInfo')
        isApproved = False
        username = User.objects.get(pk=user)

        organizerReq = RequestOrganizer(hospitalName=hospitalName, hospitalAddress=hospitalAddress, businessEmail=businessEmail,
                                contactInfo=contactInfo, isApproved=isApproved, username=username)
        
        organizerReq.save()

        return render(request, self.template_name,{'user': user})


