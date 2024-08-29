from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('email', 'subject')
    readonly_fields = ('name', 'email', 'mobile_no', 'subject', 'message')
