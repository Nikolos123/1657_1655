import datetime
import logging

import requests
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from authapp.models import User
from geekshop.celery import app

logger = logging.getLogger(__name__)




@app.task
def send_to_email(email:str,activation_key:str,username:str) -> None:  # не передаем рез
    verify_link = reverse('authapp:verify',
                          args=[email, activation_key])
    subject = f'Для активации учетной записи {username} пройдите по ссылки'
    message = f'Для подтверждения учетной записи {username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email],
                  fail_silently=False)
    except Exception as f:
        logger.warning(f'user send_to_email{f}')
        return f
    logger.debug(f'user send_to_email{username}')
    print(f'user send_to_email{username}')

@app.task
def distribution():  # рассылка сообщений или отчетов или еще что-то

    users = User.objects.all()
    for user in users:
        if user.is_active():
            subject = 'Рассылка'
            message = f'Ваш юзер активирован{user}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email],
                      fail_silently=False)
            logger.debug(f'user distribution{user.username}')