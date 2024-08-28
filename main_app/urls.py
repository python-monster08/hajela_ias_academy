from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/', views.course_detail, name='course-detail'),
    path('our-team/', views.our_team, name='our-team'),
]
