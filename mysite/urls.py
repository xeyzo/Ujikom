from django.urls import path, include
from django.contrib import admin

from aplikasi import views

urlpatterns = [
    path(r'daftar/create/', views.daftar_create, name='daftar_create'),
    path('pembayaran/', views.pembayaran, name='pembayaran'),
    path('pasien/', views.pasien, name='pasien'),
    path('pendaftaran/', views.pendaftaran, name='pendaftaran'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
