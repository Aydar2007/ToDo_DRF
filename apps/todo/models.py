from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.

User = get_user_model()

class ToDo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_todo',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )


    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таск"
