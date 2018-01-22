# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from .models import Score

class ScoreListView(ListView):
    model = Score
    template_name = 'home.html'
