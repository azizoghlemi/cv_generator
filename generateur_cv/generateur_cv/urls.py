"""generateur_cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *
from django.contrib import admin
from django.urls import path
from generateur_cv.views import *
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ba3dou),
    path('formp0.html',landing),
    path('engformp1.html', eng1),
    path('engformp2.html', eng2),
    path('engformp3.html', eng3),
    path('engformp4.html', eng4),
    path('engformp5.html', eng5),
    path('engformp6.html', eng6),
    path('engformp7.html', eng7),
    path('engformp8.html', eng8),
    path('engformp9.html', eng9),
    path('engformp10.html', eng10),
    path('engformp11.html', eng11),
    path('engformp12.html', eng12),


    path('arformp1.html', ar1),
    path('arformp2.html', ar2),
    path('arformp3.html', ar3),
    path('arformp4.html', ar4),
    path('arformp5.html', ar5),
    path('arformp6.html', ar6),
    path('arformp7.html', ar7),
    path('arformp8.html', ar8),
    path('arformp9.html', ar9),
    path('arformp10.html', ar10),
    path('arformp11.html', ar11),
    path('arformp12.html', ar12),


    path('frformp1.html', fr1),
    path('frformp2.html', fr2),
    path('frformp3.html', fr3),
    path('frformp4.html', fr4),
    path('frformp5.html', fr5),
    path('frformp6.html', fr6),
    path('frformp7.html', fr7),
    path('frformp8.html', fr8),
    path('frformp9.html', fr9),
    path('frformp10.html', fr10),
    path('frformp11.html', fr11),
    path('frformp12.html', fr12),

    path('arcv.html', arcv),
    path('engcv.html', engcv),
    path('frcv.html', frcv),
    path('engpdf_view/', views.engViewPDF.as_view(), name="engpdf_view"),
    path('arpdf_view/', views.arViewPDF.as_view(), name="arpdf_view"),
    path('frpdf_view/', views.frViewPDF.as_view(), name="frpdf_view"),
]
