from __future__ import unicode_literals

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=750)
