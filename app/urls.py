"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myurl.views import MyUrlList, MyUrlAdd, MyURLUpdate, MyURLDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(MyUrlList.as_view()),name='myurl-list'),
    path('admin/', admin.site.urls),
    path('myurls/', login_required(MyUrlList.as_view())),
    path('myurls/add/', login_required(MyUrlAdd.as_view()), name='myurl-add'),
    path('myurls/<int:pk>/', login_required(MyURLUpdate.as_view()), name='myurl-update'),
    path('myurls/delete/<int:pk>/', login_required(MyURLDelete.as_view()), name='myurl-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]
