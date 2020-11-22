"""AME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from protocolo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='url_index'),
    path('stroop/', views.Stroop, name='url_stroop'),
    path('stroop_teste/<cod>',views.Stroop1, name='url_stroop1'),
    path('stroop_resultados/<cod>', views.Stroop2, name='url_stroop2'),
    path('stroop_try/', views.StroopTry, name='url_strooptry'),
    path('form/', views.Form, name='url_form'),
    path('exercicios/', views.Exercicios0, name='url_exercicios'),
    path('exercicios/<cod>', views.Exercicios, name='url_exercicios'),
]
