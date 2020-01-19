# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from feedback.forms import ScoreForm
from feedback.models import VideoUrl,ScoreOneStimulus
#################BackEnd Functionality###################################

video_id_list = ['0001','0002','0003']
def checkUserExists(username):
#To check if newuser or existing user?
	obj=ScoreOneStimulus.userScore.filter(user_name=username)
	# print(obj)
	if(len(obj)==0):
		return 'newuser'
	else:
		return 'existinguser'
# def NewEntry(username,video_id_list):
# #To insert initial data into the table 
# 	for item in video_id=_list:
# 		obj=ScoreOneStimulus(user_name=username,session_id=1,vid_id=item)
# 		obj.save()

def NewEntry(username):
	#To insert initial data into the table
	for item in video_id_list:
		obj = ScoreOneStimulus(user_name=username, session_id=1, vid_id=item)
		obj.save()
def checkSession(username):
#To check if its new session or old session
	obj=ScoreOneStimulus.userScore.filter(user_name=username).filter(score__isnull=True)
	if(len(obj)==0):
		return ('newsession','Dummy')
	else:
		vid_sublist=[]
		for item in obj:
			vid_sublist.append(item.vid_id)
		return ('oldsession',vid_sublist)
	# print(len(obj))
	# return
def incSessionId(username):
	#To increment sessionid after fetching last session id
	obj=ScoreOneStimulus.userScore.filter(user_name=username).order_by('-session_id')[0]
	return (obj.session_id +1)

def fetchVideo(video_id_list):
#To fetch video url from database corresponding to each video id
	vid_url_list= []
	for item in video_id_list:
		print(item)
		vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
	return vid_url_list
def findSessionId(username):
#To find last session id
	obj=ScoreOneStimulus.objects.filter(user_name=username).order_by('-session_id')[0]
	# print(obj.session_id)
	return obj.session_id

def updateScore(username,sid,vid,scr):
# To update score in the database table
	obj=ScoreOneStimulus.userScore.get(user_name=username,session_id=sid,vid_id=vid)
	# print(obj.score)
	obj.score=scr
	obj.save()
	return
# func1('a130')
# func2('a005',['0001','0002','0007','0002','0018'])
# print('next session',func4('a101'))
# print(func3('a130'))
# func7('a101',1,'0001',9)
# func6('a101')
# print('Function5',func5(['0001','0003']))











class score(TemplateView):
	template_name = 'sample.html'

	def get(self, request):
		form = ScoreForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = ScoreForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = ScoreForm()
			return redirect('sample')
		args = {'form': form, 'text' : text}	
		return render(request, self.template_name, args)



