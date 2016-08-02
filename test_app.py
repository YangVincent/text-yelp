import unittest
from yelp_and_chill import app

# Import an XML Parser
from xml.etree import ElementTree

class TwiMLTest(unittest.TestCase):
    def setUp(self):
        # Create a test app every time
        self.test_app = app.test_client()

    def assertTwiML(self, response):
        # Check for error
        self.assertEquals(response.status, "200 OK")
        root = ElementTree.fromstring(response.data)
        self.assertEquals(root.tag, 'Response', 
                "Did not find tag as root element" \
                "TwiML Rseponse")

    def message(self, body, url='/', to="+16503977854", from_='+14082032094', extra_params={}):
        """Simulates Twilio Message request to Flask test client
 
        Args:
            body: The contents of the message received by Twilio.
 
        Keyword Args:
            url: The webhook endpoint you wish to test. (default '/sms')
            to: The phone number being called. (default '+16503977854')
            from_: The CallerID of the caller. (default '+14082032094')
            extra_params: Dictionary of additional Twilio parameters you
                wish to simulate, like MediaUrls. (default: {})
 
        Returns:
            Flask test client response object.
        """
 
        # Set some common parameters for messages received by Twilio.
        params = {
            'MessageSid': 'SMtesting',
            'AccountSid': 'ACxxxxxxx',
            'To': to,
            'From': from_,
            'Body': body,
            'NumMedia': 0,
            'FromCity': 'SAN DIEGO',
            'FromState': 'CA',
            'FromCountry': 'US',
            'FromZip': '92122'}
 
        # Add extra params not defined by default.
        if extra_params:
            params = dict(params.items() + extra_params.items())
 
        # Return the app's response.
        return self.test_app.post(url, data=params)
 
class TestYelpAndChill(TwiMLTest):
    def test_yelp_and_chill(self):
        # Check response tag
        response = self.message(url='/', body='usage')
        self.assertTwiML(response)
    
    def test_usage_valid(self):
        response = self.message(url='/', body='usage')
        self.assertEquals('usage' in response.data.decode("utf-8"), True)
        self.assertEquals('yacusage' in response.data.decode("utf-8"), True)
        self.assertEquals('detailusage' in response.data.decode("utf-8"), True)

    def test_random_valid(self):
        bod = 'random \nSan Diego\nEscape Room\n2'
        response = self.message(url='/', body=bod)
        self.assertEquals('Powered by Yelp' in response.data.decode("utf-8"), True)

    def test_yac_valid(self):
        bod = 'yac \nsan diego\nescape room'
        response = self.message(url='/', body=bod)
        self.assertEquals('Escape' in response.data.decode("utf-8"), True)
        self.assertEquals('Powered by Yelp' in response.data.decode("utf-8"), True)

    def test_detail_valid(self):
        bod = 'detail\nSan Diego\nSummer\'s deli'
        response = self.message(url='/', body=bod)
        self.assertEquals('Phone:' in response.data.decode("utf-8"), True)
        self.assertEquals('Address' in response.data.decode("utf-8"), True)
        self.assertEquals('reviews' in response.data.decode("utf-8"), True)
        self.assertEquals('/5' in response.data.decode("utf-8"), True)

    def test_direction_valid(self):
        bod = 'direction\nSunnyvale public library, Sunnyvale, ca\nHomestead high school, Cupertino, ca\ndriving'
        response = self.message(url='/', body=bod)
        self.assertEquals('Start from' in response.data.decode("utf-8"), True)
        self.assertEquals('End at' in response.data.decode("utf-8"), True)
        self.assertEquals('Duration' in response.data.decode("utf-8"), True)
        self.assertEquals('Distance' in response.data.decode("utf-8"), True)
        self.assertEquals('Destination' in response.data.decode("utf-8"), True)

