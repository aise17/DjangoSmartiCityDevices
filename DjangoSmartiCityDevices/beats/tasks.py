# Create your tasks here
from __future__ import absolute_import, unicode_literals



from celery import shared_task




@shared_task
def celery_taskA(counter):

    return '{} Done!'.format(counter)