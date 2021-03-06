from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """
    Custom User model with email rather than username. 
    """
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_recent_searches(self):
        searches = self.search_history.order_by('-search_date').values('query')[:5]
        return searches

    def save(self, *args, **kwargs):
        """Generate a random id of length 10 of numerical characters"""
        if not self.username:
            append_num = 1
            email_tag = self.email.split('@')[0]
            while True:
                prepend = '' if append_num == 1 else str(append_num)
                username = email_tag + prepend
                if not User.objects.filter(username=username).exists():
                    break
                append_num += 1
            self.username = username
        super(User, self).save(*args, **kwargs)

class UserPreferences(models.Model):
    """
    Model to store preferences for a User model.
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='preferences'
    )
    email_consent = models.BooleanField(null=True)