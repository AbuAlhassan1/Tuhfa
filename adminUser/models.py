from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class adminManager(UserManager):
    def create_user(self, full_name, email, password, phone):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model()
        user.full_name = full_name
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.phone = phone
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, phone=None, full_name=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model()
        user.full_name = full_name
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.phone = phone
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class AdminUser(AbstractUser, models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = adminManager()
    
    def __str__(self):
        return str(self.full_name) + " [ " + str(self.email) + " ]"