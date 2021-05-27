from __future__ import unicode_literals
from django.db import models


class Model(models.Model):
    foreign_key = models.ForeignKey('auth.User', null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    many_to_many = models.ManyToManyField('auth.User', blank=True, related_name='+')
