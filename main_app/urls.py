from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/', views.course_detail, name='course-detail'),
    path('our-team/', views.our_team, name='our-team'),
    path('gallery/images/', views.gallery_images_view, name='gallery_images'),
    path('gallery/videos/', views.gallery_videos_view, name='gallery_videos'),
]
