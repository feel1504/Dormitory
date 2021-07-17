"""mylogin URL Configuration

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
from django.urls import path,re_path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.denglu),
    path('register/',views.zhuce),
    path('login_data/', views.login),
    path('register_data/',views.register),

    path('add_stu/',views.add_student),
    re_path('student/(\d+)',views.list_student),
    re_path('edit_stu/(\d+)',views.edit_student),
    re_path('del/(\d+)',views.del_student),
    path('search_data/',views.search_data),

    path('add_emp/',views.add_emp),
    re_path('emp/(\d+)',views.list_emp),
    re_path('del_emp/(\d+)',views.del_emp),
    re_path('edit_emp/(\d+)',views.edit_emp),

    path('add_dor/',views.add_dor),
    re_path('dor/(\d+)',views.list_dor),
    re_path('del_dor/(\d+)',views.del_dor),
    re_path('edit_dor/(\d+)',views.edit_dor),

    path('add_pay/',views.add_pay),
    re_path('pay/(\d+)',views.list_pay),
    re_path('del_pay/(\d+)',views.del_pay),
    re_path('edit_pay/(\d+)',views.edit_pay),

    path('add_repair/', views.add_repair),
    re_path('repair/(\d+)', views.list_repair),
    re_path('del_repair/(\d+)', views.del_repair),
    re_path('edit_repair/(\d+)', views.edit_repair),
]
