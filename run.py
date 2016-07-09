#!/usr/bin/python3
import os

from flask import Flask, request, redirect
import twilio.twiml

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
        consumer_key=os.environ["consumer_key"],
        consumer_secret=os.environ["consumer_secret"],
        token=os.environ["token"],
        token_secret=os.environ["token_secret"]
)
client = Client(auth)

app = Flask(__name__)

callers = {
  "+14082032094": "Vincent Yang"
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #""" respond to incoming calls with a simple text message. 
    #>>> hello_monkey() != None
    #True
    #"""
    #'<?xml version="1.0" encoding="UTF-8"?><Response><Sms>SMS Hello Monkey</Sms></Response>'

    #from_number = request.values.get('From', None)
    from_number = request.values.get('From')
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "stranger, thanks for the message!"
        
    bod = request.form.get('Body')
    if 'yac' in bod:
        message = "getting yelp results!\n"

        params = {
                'term': 'food',
                'lang': 'en'
        }
        resp = client.search('San Francisco', **params)
        total = []
        for each in resp.businesses:
            total.append(each.name)
        
        new_line = '\n'
        message = message + new_line.join(total)




    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
