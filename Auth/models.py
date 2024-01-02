from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, **data):
        email = data.get("email")
        password = data.get("password")
        print(data)

        if not email:
            raise ValueError("Users must have an email address")
        data.pop("email")
        user = self.model(email=self.normalize_email(email), **data)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **data):
        email = data.get("email")
        password = data.get("password")
        if not email:
            raise ValueError("Users must have an email address")
        user = self.create_user(**data)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    website = models.URLField(default="https://google.com", blank=True, null=True)
    phone_num = models.CharField(max_length=255)
    tin = models.CharField(max_length=255)
    trade_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sector = models.CharField(
        max_length=255,
        choices=[
            ("Manufacturing", "Manufacturing"),
            ("Factory", "Factory"),
            ("Hotel", "Hotel"),
        ],
    )
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
