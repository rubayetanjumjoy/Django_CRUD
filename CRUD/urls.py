 
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls'))
]
