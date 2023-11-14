from celery import shared_task

from well.models import Course, Subscription
from user.models import User


@shared_task
def subscriber_notice(course_id):
    """
    Уведомление подписчиков об изменениях курса
    """

    course = Course.objects.get(pk=course_id)  # получаем данные об измененном курсе

    subscriptions = Subscription.objects.filter(course=course_id)  # получаем подписки на данный курс

    # если подписки существуют, отправляем подписчикам курса сообщение об изменениях
    if subscriptions:
        for subscription in subscriptions:

            print(f'Привет, {subscription.user}! В курсе "{course.course_title}" произошли изменения. '
                  f'Заходи узнать что-нибудь новое для себя')