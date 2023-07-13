from time import sleep
from celery import shared_task

@shared_task
def notify_customer(message):
    print('sending q0k emails')
    print(message)
    sleep(10)
    print('emails were sucessfully sent!')