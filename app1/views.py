from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm




# Create your views here.




def home(request):
    return render(request, 'app1/homepage.html')

def AdminLogin(request):

    return render(request, 'app1/admin_login.html')

def AdminRegistration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'app1/admin_registration.html', context)

def DocLogin(request):
    return render(request, 'app1/doc_login.html')

def DocRegistration(request):
    return render(request, 'app1/doc_registration.html')

def PatientLogin(request):
    return render(request, 'app1/patient_login.html')

def PatientRegistration(request):
    return render(request, 'app1/patient_registration.html')

def AdminDashboard(request):
    return render(request, 'app1/admin_dashboard.html')

def DoctorDashboard(request):
    return render(request, 'app1/doctor_dashboard.html')

def PatientDashboard(request):
    return render(request, 'app1/patient_dashboard.html')


