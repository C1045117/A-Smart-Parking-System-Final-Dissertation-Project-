"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.views import register, index, user_login, my_smart_parking
from booking.views import parking_reservation, parking_spot, booking_confirmation, create_booking, confirmed_bookings
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('booking/', parking_reservation, name='booking'),
    path('', my_smart_parking, name='my_smart_parking'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('index/', index, name='index'),
    path('parking_spot/<str:parking_spot_label>/', parking_spot, name='parking_spot'),
    path('booking_confirmation/<str:order_number>/', booking_confirmation, name='booking_confirmation'),
    path('create_booking/<str:parking_spot_label>/', create_booking, name='create_booking'),
    path('confirmed_bookings/', confirmed_bookings, name='confirmed_bookings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
