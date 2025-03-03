"""
URL configuration for Result_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_views, name='home'),
    path('add/', views.add_views, name='add'),
    path('delete/<int:id>', views.delete_views, name='delete'),
    path('edit/<int:id>', views.edit_views, name='edit'),
    path('view/<int:id>', views.view, name='view'),
    path('about/', views.about, name='about'),
]
