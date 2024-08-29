from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'main_app_templates/index.html')



def about(request):
    return render(request, 'main_app_templates/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile') 
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data to the Contact model
        contact = Contact(name=name, email=email, mobile_no=mobile_no, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'main_app_templates/contact.html')


def courses(request):
    return render(request, 'main_app_templates/courses.html')

def course_detail(request):
    return render(request, 'main_app_templates/course-detail.html')


def our_team(request):
    return render(request, 'main_app_templates/our-team.html')