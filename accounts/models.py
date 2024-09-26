from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Custom User Manager
class UserManager(BaseUserManager):
    """Custom user manager to handle email as the unique identifier."""
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

# Department model
class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='department_head'
    )  # Head of department (staff)

    def __str__(self):
        return self.name

# Custom User model
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )

    username = None  # Remove the username field as we will use email instead
    email = models.EmailField(_('email address'), unique=True)  # Make email the unique identifier

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    department = models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='members'
    )  # Department relation
    staff_approval_rights = models.BooleanField(default=False)  # Whether the staff can approve quotes
    admin_approval_rights = models.BooleanField(default=False)  # Whether the admin can approve quotes

    USERNAME_FIELD = 'email'  # Set email as the field used for login
    REQUIRED_FIELDS = []  # No additional required fields

    objects = UserManager()  # Use the custom user manager

    def is_staff_approver(self):
        """ Returns True if the user is a staff member with approval rights """
        return self.user_type == 'staff' and self.staff_approval_rights

    def is_admin_approver(self):
        """ Returns True if the user is an admin with approval rights """
        return self.user_type == 'admin' and self.admin_approval_rights

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"
