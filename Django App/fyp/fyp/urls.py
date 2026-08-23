"""
URL configuration for fyp project.

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
from django.urls import path
from fyp import views
from fyp.views import predict_view,  predict_view1,predict_view2



urlpatterns = [
    path('', views.home),
    path('predict/', views.prediction),
    # path('pre',views.predict_view),
    path('pre/', predict_view),
    path('pre1/', predict_view1),
    path('pre2/', predict_view2),
]
