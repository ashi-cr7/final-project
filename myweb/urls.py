from django.urls import path
from .import views as v
 

urlpatterns = [

path('', v.home, name='home'),
path('home_copy/', v.home_copy, name='home_copy'),
path('about/', v.about, name='about'),
path('admin/', v.admin_dashboard, name='admin'),
path('base/', v.base, name='base'),
path('register/', v.register, name='register'),
path('login/', v.userlogn, name='userlogn'),
path('logout/', v.userlogout, name='uslogout'),
path('vendor_dashboard/', v.vendor_dashboard, name='vendor_dashboard'),
path('package/', v.package, name='package'),
path('contact/', v.contact, name='contact'),
path('vendor_register/', v.vendor, name='vendor_register'),
path('vendor_login/', v.vendor_login, name='vendor_login'),
path('vendor_logout/', v.vendor_logout, name='vendor_logout'),
path('tour_package/', v.tour_package, name='tour_package'),
path('package/<int:pk>/edit/', v.edit_package, name='edit_package'),
path('package/<int:pk>/delete/',v.delt,name='delt'),
path('display/',v.display,name='display'),
]