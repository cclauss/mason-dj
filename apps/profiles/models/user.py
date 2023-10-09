from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from core.enums.title import Title
from core.mixins.auto_validable import AutoValidable
from core.mixins.deactivable import Deactivable
from core.models.base_model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Custom User Manager is required when defining a custom User class"""

        user = self.model(
            email=email,
            is_superuser=False,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        # NOTE: Uncomment if you need to generate APIToken for your user
        # and make this method an atomic transaction.
        # APIToken: Any = apps.get_model("token_auth", "APIToken")
        # APIToken.objects.create(user=user)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(Deactivable, AutoValidable, PermissionsMixin, AbstractBaseUser, BaseModel):
    class Meta:
        db_table = "tb_users"
        verbose_name = "utilisateur"
        ordering = ["-created"]
        get_latest_by = "created"

    email = models.EmailField("e-mail", unique=True)
    title = models.CharField("civilité", choices=Title.choices)
    first_name = models.CharField("prénom")
    last_name = models.CharField("nom")
    phone_number = PhoneNumberField("téléphone", blank=True, null=True)
    birth_date = models.DateField("date de naissance", blank=True, null=True)
    is_staff = models.BooleanField("staff ?", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # 🔗 https://bit.ly/3w1KadY
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "title",
    ]  # 🔗 https://bit.ly/3dknLlD

    def clean(self) -> None:
        # NOTE: full_clean() is called in save() with the Autovalidable mixin
        self.email = self.email.lower()
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.upper()

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def small_name(self) -> str:
        return f"{self.first_name[0]}. {self.last_name}"

    def __str__(self):
        return self.name