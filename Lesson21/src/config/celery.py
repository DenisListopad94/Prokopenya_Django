import os

from celery import Celery, shared_task
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
#
#
# @app.task(bind=True, ignore_result=True)
# def debug_task_two(self):
#     from time import sleep
#     sleep(20)
#     print(f'Hello')


# if __name__ == "main":
#     debug_task_two()

@shared_task
def debug_task_two(second: int):
    from time import sleep
    sleep(second)
    return f'Sleep {second}'


@shared_task
def get_users(second: int):
    from time import sleep
    sleep(second)
    return f'Sleep {second}'


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    # Executes every 1 minutes
    'sleep some seconds': {
        'task': 'config.celery.debug_task_two',
        'schedule': crontab(minute="*/3,4"),
    },
}

app.conf.beat_schedule = {
    # Executes every 1 minutes
    'Say HI': {
        'task': 'config.celery.debug_task',
        'schedule': {
            'minute': '0',
            'hour': '19,20,21',
        },
    },
}
