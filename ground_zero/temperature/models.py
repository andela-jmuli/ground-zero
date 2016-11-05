from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

from datetime import datetime


class Temperature(models.Model):
    """
    model to store temperature value
    """
    temp_value = models.CharField(max_length=70)
    created_time = models.TimeField(_(u"created Time"), blank=True, default=datetime.now())
