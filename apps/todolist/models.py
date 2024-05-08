from django.db import models

from apps.users.models import User
# Create your models here.
class ToDo(models.Model):
    performing = models.ForeignKey(User, 
                                   on_delete=models.CASCADE, 
                                   verbose_name='Выполняющий таск')
    title = models.CharField(
        max_length = 255,
        verbose_name='Название задания',
        unique=True
    )
    description = models.CharField(
        max_length = 600,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='image_todo/',
        verbose_name='Фотография'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name = 'Статус выполнения'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата задания'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'
