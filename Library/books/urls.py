"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from books import views
app_name="books"

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add_book,name='add_book'),
    path('view',views.view_book,name='view_book'),
    path('add1',views.add_book1,name='add_book1'),
    path('detail/<int:i>',views.detail,name='detail'),
    path('edit/<int:i>',views.edit,name='edit'),
    path('delete/<int:i>',views.deletebook,name='delete'),
    path('search', views.searchbook, name='search'),
]
