from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    


class GalleryItem(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='gallery/', blank=True, null=True)  # Used only for images
    video_url = models.URLField(max_length=500, blank=True, null=True)  # Used only for videos
    video_thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True, null=True)  # Thumbnail for video
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        # Ensure file is used for images and video_url for videos, with optional thumbnail for video
        if self.media_type == 'image' and not self.file:
            raise ValidationError('File is required for images.')
        if self.media_type == 'video' and not self.video_url:
            raise ValidationError('Video URL is required for videos.')
        if self.media_type == 'video' and self.file:
            raise ValidationError('Video items should not have a file upload, use a video URL instead.')
        if self.media_type == 'image' and self.video_url:
            raise ValidationError('Image items should not have a video URL, upload a file instead.')

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name