from django.test import TestCase
from videoplay.models import ScoreOneStimulus, VideoUrl,ScoreTwoStimulus
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django.test import Client
from django.conf import settings
from django.http import HttpRequest


class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver =webdriver.Chrome(ChromeDriverManager().install())
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get('http://127.0.0.1:8000')
        self.client = Client()
        # self.client.login(username='ganeshraj', password='139Acolumbia')

    def test_only_login(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("login")

        # enter search keyword and submit
        self.search_field.click()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/login/')
    
    def test_only_signup(self):
        # get the search textbox
        # self.driver.get('http://127.0.0.1:8000/login')
        self.sigup = self.driver.find_element_by_name("signup")

        # enter search keyword and submit
        self.sigup.click()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/register/')

    def test_login_inside(self):

        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('ani61')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('testing123@')
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/')
        # self.agree = self.driver.find_element_by_name("vehicle")
        #     # enter search keyword and submit
        # self.agree.click()

        # self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/download/')
    
    def test_download(self):
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('ani61')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('testing123@')
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/')
        # self.agree = self.driver.find_element_by_name("Agree")
        #     # enter search keyword and submit
        # self.agree.click()
        # self.search_field = self.driver.find_element_by_name("download")
        # c = Client()
        # response = c.get(self.search_field.click())
      
        # self.assertEqual(response.status_code,200)
    
    def test_playfunction_scoreone(self):
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('ani61')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('testing123@')
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/')
        # self.agree = self.driver.find_element_by_name("Agree")
        #     # enter search keyword and submit
        # self.agree.click()
        # self.search_field = self.driver.find_element_by_name("download")
        # self.agree = self.driver.find_element_by_name("part1")
        #     # enter search keyword and submit
        # self.agree.click()
        # self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/videos/')
    
    def test_playfunction_scoretwo(self):
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('ani61')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('testing123@')
        self.search_field = self.driver.find_element_by_name("login")
    #     # enter search keyword and submit
        self.search_field.click()
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/')
        # self.agree = self.driver.find_element_by_name("Agree")
        #     # enter search keyword and submit
        # self.agree.click()
        # self.agree = self.driver.find_element_by_name("part2")
        #     # enter search keyword and submit
        # self.agree.click()
        # self.driver.implicitly_wait(70)
        # self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/videoplay/videos2/')

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
