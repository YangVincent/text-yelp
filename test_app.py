import unittest
from app import app

class TestYelpAndChill(unittest.TestCase):
    def test_yelp_and_chill(self):
        #use Flask's test client for the test
        self.test_app = app.test_client()

        #Make a test request to twilio
        response = self.test_app.post('/', data={'From': '+14082032094'})

        #Assert response is okay
        self.assertEquals(response.status, "200 OK")
