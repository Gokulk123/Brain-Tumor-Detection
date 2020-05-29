"""brain_tumor_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .brain_tumor_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('back_office_home/',views.back_office_home),
    path('agent_home/',views.agent_home),
    path('client_home/',views.client_home),
    path('client_reg/',views.client_reg),
    path('agent_reg/',views.agent_reg),
    path('client_login/',views.client_login),
    path('agent_login/',views.agent_login),
    path('back_office_login/',views.back_office_login),
    path('office_login/',views.office_login),
    path('office_logout/',views.office_logout),
    path('client_signup/',views.client_signup),
    path('agent_signup/',views.agent_signup),
    path('view_client/',views.view_client),
    path('user_active/',views.user_active),
    path('user_inactive/',views.user_inactive),
    path('view_agent/',views.view_agent),
    path('agent_active/', views.agent_active),
    path('agent_inactive/', views.agent_inactive),
    path('manage_request/', views.manage_request),
    path('view_insurance_details/', views.view_insurance_details),
    path('send_response/', views.send_response),
    path('client_signin/', views.client_signin),
    path('client_logout/', views.client_logout),
    path('agent_signin/', views.agent_signin),
    path('agent_logout/', views.agent_logout),
    path('add_insurance/', views.add_insurance),
    path('agent_add_insurance/', views.agent_add_insurance),
    path('agent_view_insurance/', views.agent_view_insurance),
    path('view_profile/', views.view_profile),
    path('update_agent_profile/', views.update_agent_profile),
    path('client_view_insurance/', views.client_view_insurance),
    path('user_profile/', views.user_profile),
    path('update_client_profile/', views.update_client_profile),
    path('add_claim/', views.add_claim),
    path('claim_values/', views.claim_values),
    path('user_claim_details/', views.user_claim_details),
    path('forward_claim/', views.forward_claim),
    path('forwared_claim_details/', views.forwared_claim_details),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)