#！/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:zhangcs
from django.conf.urls import url,include
from . import views

urlpatterns = [
	#路由至主页
	url(r'^$', views.Index),
	url(r'^(\d+)/$',views.detail),
	#路由至grades
	url(r'^grades/$',views.grades),
	#路由至students
	url(r'^students/$',views.students),
	url(r'^grades/(\d+)/$',views.gradesStudents),
]