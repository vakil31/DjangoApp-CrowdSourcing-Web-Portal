import os
import json
import random
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from videoplay.models import ScoreOneStimulus, VideoUrl,ScoreTwoStimulus
from user import views as user_views
from django.template import loader
import re
from django.shortcuts import redirect
username = ''
stat_url = ["{% static url%}"]

#Jatin's Backend code
def update_urllookup():
      data = open('static/video_list3.txt', 'r',).read()
      rows = re.split('\n', data)  # splits along new line
      for index, row in enumerate(rows):
            cells = row.split(' ')
            print(cells[0])
            print(cells[1])
            obj = VideoUrl(vid_id=cells[0], vid_url='http://' + cells[1])
            obj.save()
      return
# update_urllookup()

def randomidpicker1(n):
      completelist=[]
      for i in range(len(VideoUrl.urlobj.filter())):
            completelist.append(VideoUrl.urlobj.filter()[i].vid_id)
      # print("Complete List",completelist)
      video_lists1=list(set(random.sample(completelist,n)))
      # print(video_lists1)
      if (len(video_lists1)==n):
            return video_lists1
      else:
            randomidpicker1(n)
def randomidpicker2(n):
      #There should not be any duplicates among pairs and there should not be same video ids in single pair
      completelist=[]
      for i in range(len(VideoUrl.urlobj.filter())):
            completelist.append(VideoUrl.urlobj.filter()[i].vid_id)
      # print("Complete List",completelist)
      temp_list1=list(set(random.sample(completelist,2*n)))
      # print("Inside Random Picker2 and gonna print temp_list1...",temp_list1)
      if (len(temp_list1)==2*n):
            video_lists2 = list(zip(temp_list1[:n],temp_list1[n:2*n]))
            print("Inside Random Sampler 2...gonna print video list 2....",video_lists2)
            return video_lists2
      else:
            randomidpicker2(n)
randomidpicker2(5)
# def activelearningpicker(n):
#       pass
#       return

# print("Random Id List",randomidpicker1(5))
#don' delete this #update_urllookup()
# update_urllookup()








# video_lists = ['0000001', '0000002','0000003','0000004']
# video_lists=randomidpicker1(5)
# print("Random list for single stimulus",video_lists)
# video_lists2 = [('0000002', '0000004'),('0000001','0000003')]
# video_lists2=randomidpicker2(5)
# name_list=[('1_fps25.mp4', '2_fps24.mp4'), ('3_fps24.mp4', '4_fps25.mp4')]




def vidlist2vidname(video_lists2):
      list1=[]
      for item1 in video_lists2:
            list2=[]
            url1=VideoUrl.urlobj.filter(vid_id=item1[0])[0].vid_url
            url2=VideoUrl.urlobj.filter(vid_id=item1[1])[0].vid_url
            name1 = re.split("/", url1)[-1]
            name2 = re.split("/", url2)[-1]
            list2.append(name1)
            list2.append(name2)
            list1.append(list2)
      return list1

def uniquelistfordownload(video_lists2):
      list1=[]
      for item1 in video_lists2:
            list1.append(item1[0])
            list1.append(item1[1])
      return list(set(list1))
# print("Printing unique list\n",uniquelistfordownload(video_lists2))
# name_list=vidlist2vidname(video_lists2)
# print("name_list",name_list)


def checkUserExists_1(username):
	#To check if newuser or existing user?- For Single Stimulus
	obj = ScoreOneStimulus.userScore.filter(user_name=username)
	if(len(obj) == 0):
		return False
	else:
		return True
def checkUserExists_2(username):
	#To check if newuser or existing user?- For Double Stimulus
	obj = ScoreTwoStimulus.userPref.filter(user_name=username)
	if(len(obj) == 0):
		return False
	else:
		return True
def NewEntry_1(username,video_lists, sid=1):
	#To insert initial data into the table for single stimulus

      for item in video_lists:
            print("Inside NewEntry1 Function and gonna add ", item, "\n")
            obj = ScoreOneStimulus(
            	user_name=username, session_id=sid, vid_id=item)
            obj.save()
      return video_lists
def NewEntry_2(username,video_lists2, sid=1):
	#To insert initial data into the table for double stimulus

      for item in video_lists2:
            print("Inside NewEntry2 Function and gonna add ", item[0],item[1], "\n")
            obj = ScoreTwoStimulus(
            	user_name=username, session_id=sid, vid_id1=item[0],vid_id2=item[1])
            obj.save()
      return video_lists2
# NewEntry_2("abcd1")

def checkSession_1(username):
	#To check if its new session or old session
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).filter(score__isnull=True)
	if(len(obj) == 0):
		return ('newsession', 'Dummy')
	else:
		vid_sublist = []
		for item in obj:
			vid_sublist.append(item.vid_id)
		return ('oldsession', vid_sublist)

def checkSession_2(username):
	#To check if its new session or old session for double stimulus
	obj = ScoreTwoStimulus.userPref.filter(user_name=username).filter(preference__isnull=True)
	if(len(obj) == 0):
		return ('newsession', 'Dummy','Dummy')        
	else:
            # print(obj)
		vid_sublist = []
		for item in obj:
			vid_sublist.append((item.vid_id1,item.vid_id2))
		return ('oldsession', vid_sublist)
# print("Checking Session for double stimulus\n",checkSession_2('abcd1')[1])
def incSessionId_1(username):
	#To increment sessionid after fetching last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)
def incSessionId_2(username):
	#To increment sessionid after fetching last session id
	obj = ScoreTwoStimulus.userPref.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)

def findSessionId_1(username):
	#To find last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return obj.session_id
def findSessionId_2(username):
	#To find last session id
	obj = ScoreTwoStimulus.userPref.filter(
		user_name=username).order_by('-session_id')[0]
	return obj.session_id
# print("SessionId2\t",findSessionId_2('abcd1'))
# print("SessionId2\t",incSessionId_2('abcd1'))
def updateScore_1(username, sid, vid, scr):
	# To update score in the database table
      print("Inside update score, gonna update score for id",vid)
      obj = ScoreOneStimulus.userScore.get(user_name=username, session_id=sid, vid_id=vid)
      obj.score = scr
      obj.save()
      print("Score updated in backend Bingo!!!")
      return
def updatePref_2(username, sid, vid1,vid2, pref):
	# To update score in the database table
      print(username)
      print(sid)
      print(vid1)
      print(vid2)
      obj = ScoreTwoStimulus.userPref.get(user_name=username, session_id=sid, vid_id1=vid1,vid_id2=vid2 )
      obj.preference = pref
      obj.save()
      print("Pref is updated in backend Bingo!!!")
      return
# updatePref_2('abcd121',1,'0000003','0000001','0000003')
def backendlogic_1(username):
      # For Single Stimulus
      video_lists=randomidpicker1(4)
      if checkUserExists_1(username) == False:
            NewEntry_1(username,video_lists)
            return video_lists
      else:
            if(checkSession_1(username)[0] == 'oldsession'):
                  return checkSession_1(username)[1]
            else:
                  sid = incSessionId_1(username)
                  return NewEntry_1(username,video_lists, sid)
def backendlogic_2(username):
      # For Double Stimulus
      print("Inside Backend logic2")
      video_lists2=randomidpicker2(5)
      if checkUserExists_2(username) == False:
            NewEntry_2(username,video_lists2)
            return video_lists2
      else:
            if(checkSession_2(username)[0] == 'oldsession'):
                  return checkSession_2(username)[1]
            else:
                  sid = incSessionId_2(username)
                  return NewEntry_2(username,video_lists2, sid)


def getvid(videoname):
      #To get vid id from database for given video name"
      # print("Given below is the url for reverselookup")
      # print('http://vision-pc4.eng.uwaterloo.ca:/videos/'+videoname)
      # vid=VideoUrl.urlobj.get(vid_url='http://vision-pc4.eng.uwaterloo.ca:/videos/'+videoname).vid_id
      vid=VideoUrl.urlobj.filter(vid_url__contains="/"+videoname)
      print(vid[0].vid_id)
      return vid[0].vid_id
def fetchVideo(video_id_list):
      #To fetch video url from database corresponding to each video id
      vid_url_list = []
      print("I am inside Fetch Video Function\n")
      for item in video_id_list:
            print(item)
            vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
      return vid_url_list
# print(fetchVideo(video_lists))

def download(request):
      print(request.user)
      print("I am inside download1 and gonna call backened logic1")
      video_lists1 = backendlogic_1(request.user)
      print(video_lists1)
      urls = fetchVideo(video_lists1)
      print(urls)
      context1 = {}
      context1['urls'] = ','.join([str(i) for i in urls])
      return render(request, 'videoplay/download.html', context1)


def download2(request):
      print(request.user)
      print("I am inside download2 and gonna call backened logic2")
      video_lists2 = backendlogic_2(request.user)
      # print(video_lists2)
      uniquelist=uniquelistfordownload(video_lists2)
      # print("unique list",uniquelist)
      urls = fetchVideo(uniquelist)
      # print("Double stimulus urls",urls)
      name_list=vidlist2vidname(video_lists2)
      context1 = {}
      context1['name_list'] = ','.join([str(i) for i in name_list])
      context1['urls'] = ','.join([str(i) for i in urls])
      return render(request, 'videoplay/download2.html', context1)

# Create your views here.
def home(request):
    return render(request, 'videoplay/home.html')


def agree(request):
    return render(request, 'videoplay/agreement.html')



def play_for_single(request):
      dummy = backendlogic_1(request.user)
      if request.method == 'POST':
            query = json.loads(request.POST['score'])
            query1=(request.POST['fileName'])
            print(query)
            print("vid returned from frontend",query1)
            updateScore_1(request.user, findSessionId_1(request.user), getvid(query1), query)
            message = "Thank You for watching! {}".format(query)
            context = {'message': message, }
            return render(request, 'videoplay/play.html', context)
      return render(request, 'videoplay/play.html')


def play_for_double(request):
      #backend logic2 is called again in order to make sure name_list & video_list is same in download2 as well as play_for_double
      video_lists2 = backendlogic_2(request.user)
      name_list=vidlist2vidname(video_lists2)
      context = {}
      context['name_list'] = ','.join([str(i) for i in name_list])
      if request.method == 'POST':
            # query = json.loads(request.POST['score'])
            # query1=(request.POST['fileName'])
            vid1=getvid(request.POST['vid_name1'])
            vid2=getvid(request.POST['vid_name2'])
            print(vid1)
            print(vid2)
            print(request.user)
            pref=json.loads(request.POST['preference'])
            # updatePref_2(request.user, 1, vid1,vid2, vid1)
            if(pref=='1'):
                  updatePref_2(request.user, findSessionId_2(request.user), vid1,vid2, vid1)
                  print("Bingo")
            elif(pref=='2'):
                  updatePref_2(request.user, findSessionId_2(request.user), vid1,vid2, vid2)
                  print('bingo!')
            else:
                  print("Enter Wrong Preference")
            # print(query)
            # print(query1)
            
            # updateScore_1(request.user, findSessionId_1(request.user), getvid(query1), query)
            return render(request, 'videoplay/play2.html', context)
      return render(request, 'videoplay/play2.html',context)

def temp(request):
      return render(request, 'videoplay/temp.html')


def temp2(request):
      return render(request, 'videoplay/temp2.html')

def preference(request):
      # if request.method == 'POST':
      #       query = json.loads(request.POST['score'])
      #       print(query)
      #       message = "Thank You for watching! {}".format(query)
      #       context = {'message': message, }
      #       return render(request, 'videoplay/temp.html', context)
      return render(request, 'videoplay/preference.html')


def randomidpicker1(n):
      completelist=[]
      for i in range(len(VideoUrl.urlobj.filter())):
            completelist.append(VideoUrl.urlobj.filter()[i].vid_id)
      # print("Complete List",completelist)
      video_lists1=list(set(random.sample(completelist,n)))
      # print(video_lists1)
      if (len(video_lists1)==n):
            return video_lists1
      else:
            randomidpicker1(n)
def activelearningpicker(n):
      pass
      return

# print("Random Id List",randomidpicker1(10))
#don' delete this #update_urllookup()
#update_urllookup()
