"""
URL configuration for the project.

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
import os
from django.contrib import admin
from django.urls import include, path
from project.utils.decorators import decorator_include, group_required

urlpatterns = [
    path("polls/", decorator_include(group_required("example"), "polls.urls")),
    path('accounts/', include('allauth.urls')),
    path(os.getenv("PROJECT_ADMIN_PATH"), admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("home.urls")),
]
