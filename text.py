#!/usr/bin/python3
from twilio.rest import TwilioRestClient
import os

account_sid = os.environ.get("TWILIO_ACCT")
auth_token = os.environ.get("TWILIO_TOKEN")
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14082032094", from_="+16503977854", body="hello from Vincent's Twilio!")

