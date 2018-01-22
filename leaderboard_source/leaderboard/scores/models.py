# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Score(models.Model):
    class Meta:
            ordering = ['-player_score']
    
    name = models.CharField(max_length=100, primary_key=True)
    player_score = models.IntegerField()

    def __str__(self):
        return self.name
