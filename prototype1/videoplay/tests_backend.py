from django.test import TestCase
from videoplay.models import ScoreOneStimulus, VideoUrl,ScoreTwoStimulus
import videoplay.views as views
import re
import unittest
class ScoreOneStimulusTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        line1=ScoreOneStimulus.userScore.create(user_name="test01", session_id=1, vid_id="vid_001",score=98)
        line2=ScoreOneStimulus.userScore.create(user_name="test01", session_id=1, vid_id="vid_002",score=99)
        line3=ScoreOneStimulus.userScore.create(user_name="test02", session_id=1, vid_id="vid_003",score=58)
        line4=ScoreOneStimulus.userScore.create(user_name="test02", session_id=1, vid_id="vid_004",score=78)
        line5=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_005",score=88)
        line6=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_006")
        line7=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_007")
        views.update_urllookup()
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    def test_Score_Table_Intialization(self):
        line1=ScoreOneStimulus.userScore.get(user_name="test01", session_id=1, vid_id="vid_001")
        score=line1.score
        self.assertEqual(score, 98)
    def test_CheckUserExists_1(self):
        self.assertTrue(views.checkUserExists_1("test01"))
        self.assertFalse(views.checkUserExists_1("random"))
    def test_checkSession_1(self):
        self.assertEqual(views.checkSession_1("test01")[0],"oldsession")
        self.assertEqual(views.checkSession_1("test01")[1],["vid_006","vid_007"])
        self.assertEqual(views.checkSession_1("test02")[0],"newsession")
    def test_findSession_1(self):
        self.assertEqual(views.findSessionId_1("test01"),2)
        self.assertEqual(views.findSessionId_1("test02"),1)
    def test_incSession_1(self):
        self.assertEqual(views.incSessionId_1("test02"),2)
    def test_NewEntry_1(self):
        entrylist=views.NewEntry_1("test_new",["vid_1","vid2","vid3"])
        self.assertEqual(entrylist,["vid_1","vid2","vid3"])
    def test_updateScore_1(self):
        views.updateScore_1("test01", 2, "vid_006", 98)
        obj=ScoreOneStimulus.userScore.get(user_name="test01", session_id=2, vid_id="vid_006")
        self.assertEqual(obj.score,98)
    def test_backendlogic_1(self):
        self.assertEqual(views.backendlogic_1("test01"),["vid_006","vid_007"])
        self.assertEqual(len(views.backendlogic_1("test02")),4)
        self.assertEqual(len(views.backendlogic_1("random")),4)
    def test_randomidpicker1(self):
        self.assertEqual(len(views.randomidpicker1(3)),3)
    # def test_activelearningpicker(self):
    #     self.assertEqual(views.activelearningpicker(3),3)




class ScoreTwoStimulusTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        line1=ScoreTwoStimulus.userPref.create(user_name="test01", session_id=1, vid_id1="vid_001",vid_id2="vid_002",preference="vid_001")
        line2=ScoreTwoStimulus.userPref.create(user_name="test01", session_id=1, vid_id1="vid_003",vid_id2="vid_004",preference="vid_003")
        line3=ScoreTwoStimulus.userPref.create(user_name="test02", session_id=1, vid_id1="vid_001",vid_id2="vid_002",preference="vid_002")
        line4=ScoreTwoStimulus.userPref.create(user_name="test02", session_id=1, vid_id1="vid_003",vid_id2="vid_004",preference="vid_004")
        line1=ScoreTwoStimulus.userPref.create(user_name="test01", session_id=2, vid_id1="vid_005",vid_id2="vid_006",preference="vid_005")
        line1=ScoreTwoStimulus.userPref.create(user_name="test01", session_id=2, vid_id1="vid_007",vid_id2="vid_008")
        line1=ScoreTwoStimulus.userPref.create(user_name="test01", session_id=2, vid_id1="vid_009",vid_id2="vid_010")
        # line4=ScoreOneStimulus.userScore.create(user_name="test02", session_id=1, vid_id="vid_004",score=78)
        # line5=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_005",score=88)
        # line6=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_006")
        # line6=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_007")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    def test_Score_Table_Intialization(self):
        line1=ScoreTwoStimulus.userPref.get(user_name="test01", session_id=1, vid_id1="vid_001",vid_id2="vid_002")
        pref=line1.preference
        self.assertEqual(pref, "vid_001")
    def test_CheckUserExists_2(self):
        self.assertTrue(views.checkUserExists_2("test01"))
        self.assertFalse(views.checkUserExists_2("random"))
    def test_checkSession_2(self):
        self.assertEqual(views.checkSession_2("test01")[0],"oldsession")
        self.assertEqual(1,1)
        self.assertEqual(views.checkSession_2("test01")[1],[('vid_007', 'vid_008'), ('vid_009', 'vid_010')])
        self.assertEqual(views.checkSession_2("test02")[0],"newsession")
    def test_findSession_1(self):
        self.assertEqual(views.findSessionId_2("test01"),2)
        self.assertEqual(views.findSessionId_2("test02"),1)
    def test_incSession_2(self):
        self.assertEqual(views.incSessionId_2("test02"),2)
    def test_NewEntry_2(self):
        entrylist=views.NewEntry_2("test_new",[("vid_1","vid2"),("vid3","vid1"),("vid4","vid5")])
        self.assertEqual(entrylist,[("vid_1","vid2"),("vid3","vid1"),("vid4","vid5")])
    def test_updatePref_2(self):
        views.updatePref_2("test01", 2, "vid_007","vid_008", "vid_008")
        obj=ScoreTwoStimulus.userPref.get(user_name="test01", session_id=2, vid_id1="vid_007",vid_id2="vid_008")
        self.assertEqual(obj.preference,"vid_008")
    def test_backendlogic_2(self):
        self.assertEqual(views.backendlogic_2("test01"),[('vid_007', 'vid_008'), ('vid_009', 'vid_010')])
        self.assertEqual(views.backendlogic_2("test02"),views.video_lists2)
        self.assertEqual(views.backendlogic_2("random"),views.video_lists2)

class VideoUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        line1=VideoUrl(vid_id="0000001",vid_url="http:/testurl1")
        line2=VideoUrl(vid_id="0000002",vid_url="http:/testurl2")
        line1.save()
        line2.save()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    def test_getvid(self):
        self.assertEqual(views.getvid("testurl1"), "0000001")
    def test_fetchvideo(self):
        self.assertEqual(views.fetchVideo(["0000001"]),['http:/testurl1'])
    # def test_vidlist2vidname(self,video_lists2=[('0000001', '0000002')]):
    #     self.assertEqual(views.vidlist2vidname(video_lists2),["testurl1","testurl2"])

    # if __name__ == '__main__':
    #     unittest.main()

    





