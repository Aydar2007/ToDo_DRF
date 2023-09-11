from django.db import models

from django.contrib.auth.models import AbstractUser,Permission,Group
import secrets

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True
    )
    number = models.CharField(
        max_length=15,
        verbose_name="Телефоный номер"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('Группа'),
        blank=True,
        help_text=('Группы, к которым принадлежит этот пользователь'),
        related_name='custom_user_set_groups', 
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('Разрешение'),
        blank=True,
        help_text=('Разрешение для определенных пользователей'),
        related_name='custom_user_set_permissions',  
    )
    # ...



    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"


