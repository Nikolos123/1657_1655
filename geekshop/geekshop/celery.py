"""Модуль отвечающий за настройки celery"""

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geekshop.settings')

app = Celery('geekshop')#Имя проекта get settings from settings
app.config_from_object('django.conf:settings',namespace='CELERY')#namespace
app.autodiscover_tasks()#Автоматом подцеплять наши задачи(tasks)
