"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
#Creating Router Object , which wil responsible for routing all the required path.
router=DefaultRouter()

#Registering Studentviewset with Router
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #when we are using seesion authentication we got no option for login and we have shown 
    #invalid credentials so for login purpose we are going to use inbuild method
    path('auth/',include('rest_framework.urls',
    namespace='rest_framework')),
    path('gettoken/',obtain_auth_token)#[6]Token athentication,API endpoint
]    
