from django.conf import settings
from django.db import models
from user.models import User
from user.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to='previews/')
    video_link = models.URLField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return self.title

class Payment(models.Model):
    CASH = 'CASH'
    BANK = 'BANK'

    PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (BANK, 'Перевод'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                             verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Урок')

    amount = models.IntegerField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=4, choices=PAYMENT_METHOD_CHOICES, **NULLABLE, verbose_name='способ оплаты')
    date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
