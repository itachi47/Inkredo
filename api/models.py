from django.db import models
from pyexpat import model

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Employee must have an email address")
        if not password:
            raise ValueError("Employee must a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_admin=True
        )
        return user


class Company(models.Model):
    name = models.CharField(max_length=40)
    hq = models.CharField(max_length=40)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    curr_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True)
    curr_join = models.DateField(null=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'  # username for authenticaton
    # email and password are required by default
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def getCompany(self):
        return self.company

    def setCompany(self, company):
        self.company = company

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active
