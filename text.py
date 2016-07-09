#!/usr/bin/python3
from twilio.rest import TwilioRestClient
import os

account_sid = os.environ["TWILIO_ACCT"]
auth_token = os.environ["TWILIO_TOKEN"]
print(account_sid)
print(auth_token)
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14082032094", from_="+16503977854", body="hello from Vincent's Twilio!")

