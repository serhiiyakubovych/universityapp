from django.conf.urls import url, include
from django.contrib import admin

from educational_institution import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^city/all/$', views.cities, name='cities'),
    url(r'^city/get/(?P<city_id>\d+)/$', views.city, name='city'),
    url(r'^educational_institution_type/all/$', views.educational_institution_types,
        name='educational_institution_types'),
    url(r'^educational_institution_type/get/(?P<educational_institution_type_id>\d+)/$',
        views.educational_institution_type, name='educational_institution_type'),
    url(r'^educational_direction/all/$', views.educational_directions,
        name='educational_directions'),
    url(r'^educational_direction/get/(?P<educational_direction_id>\d+)/$', views.educational_direction,
        name='educational_direction'),
    url(r'^educational_method/all/$', views.educational_methods, name='educational_methods'),
    url(r'^educational_method/get/(?P<educational_method_id>\d+)/$', views.educational_method,
        name='educational_method'),
    url(r'^faculty/all/$', views.faculties, name='faculties'),
    url(r'^faculty/get/(?P<faculty_id>\d+)/$', views.faculty, name='faculty'),
    url(r'^payment_type/all/$', views.payment_types, name='payment_types'),
    url(r'^payment_type/get/(?P<payment_type_id>\d+)/$', views.payment_type, name='payment_type'),
    url(r'^student/all/$', views.students, name='students'),
    url(r'^student/get/(?P<student_id>\d+)/$', views.student, name='student'),
    url(r'^educational_institution/all/$', views.educational_institutions, name='educational_institutions'),
    url(r'^educational_institution/get/(?P<educational_institution_id>\d+)/$', views.educational_institution,
        name='educational_institution'),
]
