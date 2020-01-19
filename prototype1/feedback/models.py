# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    post = models.CharField(max_length=3)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,)
class VideoUrl(models.Model):
    vid_id=models.CharField(max_length=10,unique=True)
    vid_url=models.CharField(max_length=256,unique=True)
    urlobj=models.Manager()

class ScoreOneStimulus(models.Model):
    user_name=models.CharField(max_length=10)
    vid_id=models.CharField(max_length=10)
    score=models.IntegerField(blank=True,null=True)
    session_id=models.IntegerField()
    userScore=models.Manager()
    def __str__(self):
        return self.vid_id