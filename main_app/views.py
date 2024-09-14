from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, TeamMember, GalleryItem
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
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
    team_members = TeamMember.objects.all()
    return render(request, 'main_app_templates/our-team.html', {'team_members': team_members})



def gallery_images_view(request):
    gallery_items = GalleryItem.objects.filter(media_type='image').order_by('-uploaded_at')
    return render(request, 'main_app_templates/gallery_images.html', {'gallery_items': gallery_items})

def gallery_videos_view(request):
    gallery_items = GalleryItem.objects.filter(media_type='video').order_by('-uploaded_at')
    return render(request, 'main_app_templates/gallery_videos.html', {'gallery_items': gallery_items})


def footer_gallery(request):
    # Fetch the latest 6 images from the GalleryItem model
    gallery_items = GalleryItem.objects.filter(media_type='image').order_by('-uploaded_at')[:6]

    context = {
        'gallery_items': gallery_items,
    }

    return context