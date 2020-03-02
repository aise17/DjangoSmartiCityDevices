import uuid

from django.db import models

# Create your models here.


class Company (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_datetime = models.DateTimeField(auto_now=True)
    url = models.URLField()
    name = models.CharField(null=True, blank=True, max_length=255)

class CompanyInfo(models.Model):
    id = models.UUIDField(primary_key=True)
    create_datetime = models.DateTimeField(auto_now=True)
    url = models.URLField()
    alexa_rank = models.PositiveIntegerField()
    email = models.CharField(null=True, blank=True, max_length=255)
    platform = models.CharField(null=True, blank=True, max_length=255)
    language = models.CharField(null=True, blank=True, max_length=255)
    status = models.PositiveIntegerField()