from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main_app_templates/index.html')



def about(request):
    return render(request, 'main_app_templates/about.html')


def contact(request):
    return render(request, 'main_app_templates/contact.html')


def courses(request):
    return render(request, 'main_app_templates/courses.html')

def course_detail(request):
    return render(request, 'main_app_templates/course-detail.html')


def our_team(request):
    return render(request, 'main_app_templates/our-team.html')