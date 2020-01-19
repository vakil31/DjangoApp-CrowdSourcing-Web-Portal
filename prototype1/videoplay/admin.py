from django.contrib import admin

# Register your models here.
from videoplay.models import VideoUrl,ScoreOneStimulus,ScoreTwoStimulus
# Register your models here.
admin.site.register(VideoUrl)
admin.site.register(ScoreOneStimulus)
admin.site.register(ScoreTwoStimulus)