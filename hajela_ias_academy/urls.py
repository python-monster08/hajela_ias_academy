from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from  django.conf.urls.static import static #new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),  # Include the main_app URLs
    path('accounts/', include('accounts.urls')),  # Include the accounts URLs
    path('question-bank/', include('question_bank.urls')),  # Include the accounts URLs
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)