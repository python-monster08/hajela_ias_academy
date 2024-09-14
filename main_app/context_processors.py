from .models import GalleryItem

def gallery_items(request):
    # Fetch the latest 6 images from the GalleryItem model
    gallery_items = GalleryItem.objects.filter(media_type='image').order_by('-uploaded_at')[:6]
    return {'gallery_items': gallery_items}
