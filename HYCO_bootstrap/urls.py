"""HYCO_bootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import homepage_view, vehicle_sales_view, about_view, contact_view, rentals_view, storage_view, detailing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage'),
    path('vehicle-sales/', vehicle_sales_view, name='vehicle-sales'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('rentals/', rentals_view, name='rentals'),
    path('storage/', storage_view, name='storage'),
    path('detailing/', detailing_view, name='detailing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
