"""lazy_balancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
#from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^dashboard/', views.view),
    url(r'^installations/', views.installations),
    url(r'^statistics/', views.statistics),
    url(r'^ip/', views.ip),
    url(r'^keys/', views.keys),
    url(r'^basesoft/', views.basesoft),
    url(r'^vms/', views.vms),
    url(r'^net/', views.net),
    url(r'^device/', views.device_view),
    url(r'^idc/$', views.idc_view),
    url(r'idc/query/$',views.idc_query),
    url(r'idc/save/$',views.idc_save),
    url(r'idc/delete/$', views.idc_delete),
    url(r'^foo/', views.foo),
    url(r'^foo_save/$',views.foo_save),
]
