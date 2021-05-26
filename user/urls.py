from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login', views.loginView.as_view(), name="login"),
    path('register', views.registerView.as_view(), name="register"),
    path('userList', views.userListView.as_view(), name="userList"),
    path('<user>/dashboard', views.dashboardView.as_view(), name="dashboard"),
    path('<user>/about', views.aboutView.as_view(), name="about"),
    path('<user>/donor', views.donorView.as_view(), name="donor"),
    path('<user>/accreditedHospital', views.accreditedHospitalView.as_view(), name="accreditedHospital"),
    path('<user>/account', views.accountView.as_view(), name="account"),
    path('<user>/requestDonor', views.requestDonorView.as_view(), name="requestDonor"),
    path('<user>/requestOrganizer', views.requestOrganizerView.as_view(), name="requestOrganizer"),
    path('<user>/editAccount', views.editAccountView.as_view(), name="editAccount"),
    path('<user>/requestAppointment', views.requestAppointmentView.as_view(), name="requestAppointment"),
    path('<user>/appointmentList', views.AppointmentView.as_view(), name="appointmentList"),
    path('<user>/editOrganizer', views.editOrganizerView.as_view(), name="editOrganizer"),
    path('<user>/editDetails', views.editDetailsView.as_view(), name="editDetails"),
    path('<user>/viewDetails', views.viewDetailsView.as_view(), name="viewDetails"),
]
