from django.contrib import admin
from .models import Contact, GalleryItem, TeamMember
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('email', 'subject')
    readonly_fields = ('name', 'email', 'mobile_no', 'subject', 'message')



@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    list_filter = ('media_type', 'uploaded_at')
    search_fields = ('title', 'description')
    ordering = ('-uploaded_at',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(GalleryItemAdmin, self).get_form(request, obj, **kwargs)
        # Customize form fields based on the media type
        if obj and obj.media_type == 'image':
            form.base_fields['file'].required = True
            form.base_fields['video_url'].required = False
            form.base_fields['video_thumbnail'].required = False
        elif obj and obj.media_type == 'video':
            form.base_fields['video_url'].required = True
            form.base_fields['file'].required = False
        return form

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')