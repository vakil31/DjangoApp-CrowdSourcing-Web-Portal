from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class VideoUrl(models.Model):
    vid_id=models.CharField(max_length=10,unique=True)
    vid_url=models.CharField(max_length=256,unique=True)
    urlobj=models.Manager()
    def __str__(self):
        return self.vid_id

class ScoreOneStimulus(models.Model):
    user_name=models.CharField(max_length=10)
    vid_id=models.CharField(max_length=10)
    score=models.IntegerField(blank=True,null=True)
    session_id=models.IntegerField()
    userScore=models.Manager()
    def __str__(self):
        return self.vid_id

class ScoreTwoStimulus(models.Model):
    session_id=models.IntegerField()
    user_name=models.CharField(max_length=10)
    vid_id1=models.CharField(max_length=10)
    vid_id2=models.CharField(max_length=10)
    preference=models.CharField(max_length=10,blank=True,null=True)
    userPref=models.Manager()
    def __str__(self):
        return self.vid_id1