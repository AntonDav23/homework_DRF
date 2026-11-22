from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        if user.is_staff is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if user.is_superuser is not True:
            raise ValueError("Суперпользователь должен иметь user.is_superuser=True")

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Укажите действующий адрес электронной почты",
    )

    phone = PhoneNumberField(
        verbose_name="Телефон",
        help_text="Укажите контактный номер телефона",
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Укажите город проживания",
        blank=True,
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        help_text="Загрузите изображение профиля",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный пользователь",
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name="Персонал",
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name = "Дата регистрации",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
