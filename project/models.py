from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class pr(models.Model):
    pr_name = models.CharField(max_length=128, null=False)
    pr_name_en = models.CharField(max_length=128, null=False)
    pr_admin = models.CharField(max_length=128, null=False)
    pr_domain = models.CharField(max_length=128, null=False)
    pr_vcs = models.CharField(max_length=128, null=False)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)