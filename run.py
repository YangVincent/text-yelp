#!/usr/bin/python3
import os
import random

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
    #>>> hello_monkey() is None
    #False
    #"""
    #'<?xml version="1.0" encoding="UTF-8"?><Response><Sms>SMS Hello Monkey</Sms></Response>'

    #from_number = request.values.get('From', None)
    from_number = request.values.get('From')
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "stranger, thanks for the message!"
        
    bod = request.form.get('Body')


    if bod == 'usage':
        message = "Usage: First line is yac\nSecond line is Current location (e.g. San Diego)\nThird line is search\nFourth line is r + number random options (e.g. r4)\nHere is an example of each request:\n\
        f"
        message = """Usage: First line is the tool you'd like to use - yac or random. Second line is the current location. Third line is your search string. Fourth line is the
        number of random options you'd like to be shown, if you chose random. Here are examples:
        yac\nSan Diego\nEscape Room\n\nrandom\nSan Diego\nEscape Room\n4
        """
    
    elif bod != None and 'yac' in bod:
        message = "No search term"

        params = {
                'lang': 'en'
        }
        if bod[bod.index('yac')+4:] != "":
            inp = bod.splitlines()
            if len(inp) > 1:
                params['term'] = inp[2]
                
            resp = client.search(inp[1], **params)
            total = []
            if resp != None:
                for each in resp.businesses:
                    total.append(each.name)

            new_line = '\n'
            message = new_line.join(total)

    
    elif bod != None and 'random' in bod:
        message = "No search term"

        params = {
                'lang': 'en'
        }
        if bod[bod.index('random')+7:] != "":
            inp = bod.splitlines()
            if len(inp) > 1:
                params['term'] = inp[2]
                
            resp = client.search(inp[1], **params)
            total = []
            if resp != None:
                for each in resp.businesses:
                    total.append(each.name)
        
            if len(inp) > 2:
                #random
                #next number after is how many options
                if inp[3].isdigit():
                    num_options = int(inp[3])
                    if num_options > len(total):
                        num_options = len(total)
                    num_remove = len(total) - num_options

                    while num_remove > 0:
                        total.remove(total[random.randrange(0, len(total)-1)])
                        num_remove = num_remove - 1

            new_line = '\n'
            message = new_line.join(total)


    resp = twilio.twiml.Response()
    resp.message('\n' + message)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
