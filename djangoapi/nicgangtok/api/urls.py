from django.contrib import admin
from django.urls import path,include
from api.views import NicgangtokViewSet,EmployeeViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'nicgangtok',NicgangtokViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls))
    
]
