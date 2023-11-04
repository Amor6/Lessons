from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

class Subscription(models.Model):
    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписки на курс'

    course_name = models.CharField(
        max_length=300, verbose_name='название подписки', **NULLABLE,
    )
    course = models.ForeignKey(
        'course.Course', verbose_name='курс для подписки', on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    user = models.ForeignKey(
        'users.User', verbose_name='пользователь', on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка оформлена')

    def __str__(self):
        return f'{self.course} {self.user}'

    def save(self, *args, **kwargs):
        self.course_name = self.course.title

        return super(Subscription, self).save(*args, **kwargs)