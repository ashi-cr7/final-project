
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def home (request):
    return render(request, 'home.html')

def home_copy(request):
    return render(request, 'home_copy.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def booking(request):
    return render(request, 'booking.html')
 
def tour_package(request):
    item = Package.objects.all()
    return render(request, 'tour_package.html', {'packages': item})

def display(request):
    item = Package.objects.all()
    return render(request, 'display.html', {'packages': item})



def vendor(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_login')
    else:
        form = VendorRegistrationForm()
    return render(request, 'vendor_register.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            Password = form.cleaned_data['password']
            if Vendor.objects.get(username=username):
                return redirect('vendor_dashboard')
    else:
        form = VendorLoginForm()
    return render(request, 'vendor_login.html', {'form': form})

def vendor_logout(request):
    logout(request)
    return redirect('vendor_login')

def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')

    




def edit_package(request, pk):
    item = get_object_or_404(Package,pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = PackageForm(instance=item)
    return render(request, 'edit_package.html', {'form': form})

def delt(request,pk):
    item = get_object_or_404(Package,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display')











def contact(request):
    return render(request, 'contact.html') 


def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogn')
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{'form':form})
    
def userlogn(request):
    if request.method == 'POST':
        form = UserloginForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_copy')
            else:
                print(f"Authentication failed for username: {username}")
                form.add_error(None, "Incorrect username or password")
    else:
        form = UserloginForm()

    return render(request, "login.html", {'form': form})

def userlogout(request):
    logout(request)
    return redirect('home')

def package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PackageForm()
    return render(request, 'package.html', {'form': form})
                      
def admin_dashboard(request):
    packages = Package.objects.all()
    return render(request, 'admin_dashboard.html', {'packages': packages})







        


