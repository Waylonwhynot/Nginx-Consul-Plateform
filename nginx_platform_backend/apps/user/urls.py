"""nginx_platform_backend URL Configuration

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
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('menu', views.MenuView, 'MenuView')
router.register('user', views.UserView, 'UserListView')
router.register('permission', views.PermissionView, 'PermissionView')
router.register('role', views.RoleView ,'RoView')
router.register('org', views.OrganizationView, 'OrgView')
urlpatterns = [
    path('', include(router.urls)),
    path('menu/tree/',views.MenuTreeView.as_view(),name='menus_tree')
]
