from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import View
from .models import *
from .forms import *

# Create your views here.



class editAccountView(View):
    template_name = "user/editAccount.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user': user})


class loginView(View):

    template_name = "user/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(pk=uname).count() != 0:
            account = User.objects.get(pk=uname)

            if account.password == pwd:
                return redirect(reverse('user:dashboard', kwargs={'user': uname}))
            else:
                messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Username Does Not Exist')

        return render(request, self.template_name)


class registerView(View):
    template_name = "user/register.html"

    def get(self, request):
        formUser = UserForm()
        return render(request, self.template_name)

    def post(self, request):
        formUser = UserForm(request.POST)
        uname = request.POST.get('username')
        password = request.POST.get('password')

        if len(uname) < 4 and len(password) < 8:
            messages.error(request, "Username and Password are too short.")
        elif User.objects.filter(pk=uname).count() != 0 and len(password) < 8:
            messages.error(
                request, "Username already exist and Password is too short.")
        elif len(uname) < 4:
            messages.error(request, "Username is too short.")
        elif User.objects.filter(pk=uname).count() != 0:
            messages.error(request, "Username already exist!")
        elif len(password) < 8:
            messages.error(request, "Password is too short.")
        else:
            customer = formUser.save(commit=False)
            customer.save()
            return redirect(reverse('user:login'))

        return render(request, self.template_name)


class userListView(View):
    template_name = "user/userList.html"

    def get(self, request):
        user = User.objects.all()
        return render(request, self.template_name, {'user': user})


class dashboardView(View):
    template_name = "user/dashboard.html"

    def get(self, request, user):
        formRequestDonor = DonorForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        donor = DonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = Donor(address=address, donorBloodType=donorBloodType,
                                isApproved=isApproved, username=username)

        donorReq.save()

        return render(request, self.template_name, {'user': user})


class aboutView(View):
    template_name = "user/about.html"

    def get(self, request, user):
        formRequestDonor = DonorForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        donor = DonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = Donor(address=address, donorBloodType=donorBloodType,
                                isApproved=isApproved, username=username)

        donorReq.save()

        return render(request, self.template_name, {'user': user})


class donorView(View):
    template_name = "user/donorList.html"

    def get(self, request, user):
        donor = Donor.objects.all()

        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        else:
            account = 0

        if Donor.objects.filter(username_id=user).count() != 0:
            donor1 = Donor.objects.get(username_id=user)
        else:
            donor1 = 0

        return render(request, self.template_name, {'donor': donor, 'user': user, 'account': account, 'donor1': donor1})


class accreditedHospitalView(View):
    template_name = "user/hospital.html"

    def get(self, request, user):
        hospital = Organizer.objects.all()
        return render(request, self.template_name, {'hospital': hospital, 'user': user})


class accountView(View):
    template_name = "user/account.html"

    def get(self, request, user):
        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        else:
            account = 0

        if Donor.objects.filter(username_id=user).count() != 0:
            donor = Donor.objects.get(username_id=user)
        else:
            donor = 0
            
        return render(request, self.template_name, {'user': user, 'account': account, 'donor': donor})

    def post(self, request, user, account):
        
            
            return render(request, self.template_name, {'user': user, 'account': account})


class requestDonorView(View):
    template_name = "user/requestDonor.html"

    def get(self, request, user):
        formRequestDonor = DonorForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        #donor = DonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        attachmentsDonor = request.POST.get('attachmentsDonor')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = Donor(address=address, donorBloodType=donorBloodType, attachmentsDonor=attachmentsDonor,
                                isApproved=isApproved, username=username)

        donorReq.save()

        return render(request, self.template_name, {'user': user})


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
        attachmentsID = request.POST.get('attachmentsID')
        attachmentsBC = request.POST.get('attachmentsBC')
        isApproved = False
        username = User.objects.get(pk=user)

        organizerReq = Organizer(hospitalName=hospitalName, hospitalAddress=hospitalAddress, businessEmail=businessEmail,
                                        contactInfo=contactInfo, attachmentsID=attachmentsID, attachmentsBC = attachmentsBC, 
                                        isApproved=isApproved, username=username)

        organizerReq.save()

        return render(request, self.template_name, {'user': user})

class requestAppointmentView(View):
    template_name = "user/requestAppointment.html"

    def get(self, request, user):
        formRequestDonor = AppointmentForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        appointment = AppointmentForm(request.POST)

        appointmentType = request.POST.get('appointmentType')
        setDate = request.POST.get('setDate')
        setTime = request.POST.get('setTime')
        isApproved = False
        #username = User.objects.get(pk=user)

        appointmentReq = RequestAppointment(appointmentType=appointmentType, setDate=setDate, setTime=setTime,
                                isApproved=isApproved)

        appointmentReq.save()

        return render(request, self.template_name, {'user': user})
