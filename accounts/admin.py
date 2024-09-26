from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Department

# Custom UserAdmin for the User model
class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('email', 'user_type', 'is_staff', 'is_superuser', 'department', 'staff_approval_rights', 'admin_approval_rights')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'department')
    
    # Customizing the fields for the form in admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Approval Rights'), {'fields': ('staff_approval_rights', 'admin_approval_rights')}),
        (_('Organizational Info'), {'fields': ('department', 'user_type')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Adding email field for user creation in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type', 'department'),
        }),
    )

    # Search fields and ordering
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Department Admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'created_at')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

# Register models with the custom admin views
admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
