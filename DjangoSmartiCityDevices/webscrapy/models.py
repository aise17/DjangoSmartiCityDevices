import json
import uuid
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_datetime = models.DateTimeField(auto_now=True)
    url = models.URLField()
    name = models.CharField(null=True, blank=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CompanyInfo(models.Model):
    id = models.UUIDField(primary_key=True)
    create_datetime = models.DateTimeField(auto_now=True)
    url = models.URLField()
    alexa_rank = models.PositiveIntegerField()
    email = models.CharField(null=True, blank=True, max_length=255)
    platform = models.CharField(null=True, blank=True, max_length=255)
    language = models.CharField(null=True, blank=True, max_length=255)
    status = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

TASKTYPE = (
    ('ITEMS', 'items'),
    ('INFO', 'info'),
)
TASKSTATUS =(
    ('LAUNCH', 'launch'),
    ('RUNING', 'runing'),
    ('FINISH', 'finish'),
    ('ERROR', 'error'),
)


class ScrapyTasks(models.Model):
    id = models.UUIDField(primary_key=True)
    create_datetime = models.DateTimeField(auto_now=True)
    finish_datetime = models.DateTimeField(auto_now=False, null=True)
    type = models.CharField(choices=TASKTYPE, max_length=255, null=True)
    status = models.CharField(choices=TASKSTATUS, max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id