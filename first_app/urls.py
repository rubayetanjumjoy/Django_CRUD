 
from django.urls import path
from django.urls.conf import include
 
from .models import Student 
from common import apis
from first_app import views
from common.apis import *
from rest_framework import routers

from . import apis
router = routers.DefaultRouter()
router.register('user', apis.List, basename='user')
app_name = 'first_app'
urlpatterns = [
    
      path('', views.index,name="index"),
      path('student_form', views.student_form,name="student_form"),
      path('student_info/<int:student_id>/', views.student_info,name="student_info"),
       path('student_update/<int:student_id>/', views.student_update,name="student_update"),
        path('student_delete/<int:student_id>/', views.student_delete,name="student_delete")
]
urlpatterns += router.urls