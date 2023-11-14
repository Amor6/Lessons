from celery import shared_task

from datetime import datetime
import pytz
import datetime

from user.models import User


@shared_task
def check_user():
    """
    Проверка пользователей на активность
    если пользователь не заходил более месяца, он блокируется
    """
    users_is_active = User.objects.filter(is_active=True)

    moscow_timezone = pytz.timezone('Europe/Moscow')  # устанавливаем часовой пояс
    date_time_now = datetime.datetime.now()  # получаем текущие дату и время
    date_now = date_time_now.astimezone(moscow_timezone)  # устанавливаем текущую дату с учетом часового пояса

    # Проверяем дату входа пользователя
    for user in users_is_active:

        # проверяем есть ли данные о последнем входе пользователя
        if user.last_login:
            # Устанавливаем дату последнего входа
            user_last_login = user.last_login.astimezone(moscow_timezone)

            # Вход более месяца
            if (date_now.date() - user_last_login.date()).days > 30:

                # "Не активен"
                user.is_active = False
                user.save()

        # Внесения даты захода пользователя
        else:
            user.last_login = date_now
            user.save()