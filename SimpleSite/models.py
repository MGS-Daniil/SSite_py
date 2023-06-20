from django.db import models

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, null=False)
    name = models.CharField(max_length=32,  unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')

    def __str__(self):
        return f"{self.name} ({self.id})"
