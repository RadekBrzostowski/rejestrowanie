# -*- coding: utf-8 -*-
from django.db import models


class Persony(models.Model):
    username = models.CharField(max_length=100, unique=True)
    birthday = models.DateTimeField()     
    parents = models.CharField(max_length=100,blank=True) 
    adult = models.BooleanField(default=1)


    def __unicode__(self):
        return ' '.join([
            self.username,
            ' ',
        ])
