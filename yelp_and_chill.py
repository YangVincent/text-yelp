#!/usr/bin/python3
import os
import random

from flask import Flask, request, redirect
import twilio.twiml

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

import googlemaps
from datetime import datetime

import simplejson as json
import re

auth = Oauth1Authenticator(
    consumer_key=os.environ["consumer_key"],
    consumer_secret=os.environ["consumer_secret"],
    token=os.environ["token"],
    token_secret=os.environ["token_secret"]
)
gmaps_key = os.environ["gmaps_key"]
client = Client(auth)

app = Flask(__name__)

callers = {
  "+14082032094": "Vincent Yang"
}

def print_usage(bod):
    usage = ['Usage:', '1st line is the tool you\'d like to use - yac, random, or detail', '2nd line is the current location (e.g. San Diego)', '3rd line is your search string',
       '4th line is the number of random options you\'d like to be shown', 'Here are examples:', '\nyac\nSan Diego\nEscape Room\n', 'will return all results for \'Escape Room\' in San Diego', 
       '\nrandom\nSan Diego\nEscape Room\n4\n', 'will return 4 random results for \'Escape Room\' in San Diego', 'Next, if you use the command detail, ', '3rd line is the name of the business',
       'will return the phone number, address, and rating for the specified business.']
    new_line = '\n'
    if 'yacusage' in bod:
        yacusage = ['yacusage:', usage[1], usage[2], usage[3], usage[5], usage[6], usage[7]]
        message = new_line.join(yacusage)
    elif 'randomusage' in bod:
        randomusage = ['randomusage:', usage[1], usage[2], usage[3], usage[4], usage[5], usage[8], usage[9]]
        message = new_line.join(randomusage)
    elif 'detailusage' in bod:
        detailusage = ['detailusage:', usage[1], usage[2], usage[11], usage[12]]
        message = new_line.join(detailusage)
    else:
        message = new_line.join(usage)
    return message

def process_yelp_and_chill(bod):
    message = "No search term"

    params = {
            'lang': 'en'
    }
    if bod[bod.index('yac')+4:] != "":
        inp = bod.splitlines()
        if len(inp) > 2:
            params['term'] = inp[2]
            
        resp = client.search(inp[1], **params)
        total = []
        if resp != None:
            for each in resp.businesses:
                total.append(each.name)

        new_line = '\n'
        message = new_line.join(total)
    return message

def process_random(bod):
    message = "No search term"

    params = {
            'lang': 'en'
    }
    if bod[bod.index('random')+7:] != "":
        inp = bod.splitlines()
        if len(inp) > 2:
            params['term'] = inp[2]
            
        resp = client.search(inp[1], **params)
        total = []
        if resp != None:
            for each in resp.businesses:
                total.append(each.name)
    
        if len(inp) > 3:
            #random
            #next number after is how many options
            if inp[3].isdigit():
                num_options = int(inp[3])
                if num_options > len(total):
                    num_options = len(total)
                num_remove = len(total) - num_options
            else:
                num_remove = len(total) - 1

            while num_remove > 0:
                total.remove(total[random.randrange(0, len(total)-1)])
                num_remove = num_remove - 1

        new_line = '\n'
        message = new_line.join(total)
    return message

def process_detail(bod):
    message = 'No search term' 
    params = {
            'lang': 'en'

    }
    if bod[bod.index('detail')+7:] != "":
        inp = bod.splitlines()
        if len(inp) > 2:
            params['term'] = inp[2]
        resp = client.search(inp[1], **params)
        if resp != None:
            bus = resp.businesses[0]
            message = '\n' + bus.name + '\nPhone: ' + bus.display_phone + '\nAddress: ' + '\n'.join(bus.location.display_address) + '\n' + str(bus.rating) + '/5 over ' + str(bus.review_count) + ' reviews'
    return message

def process_direction(bod):
    if bod[bod.index('direction') + 10:] != "":
        inp = bod.splitlines()
        if len(inp) >= 3:
            ori = inp[1]
            dest = inp[2]
            if len(inp) >= 4:
                mode = inp[3]
                if mode in ['driving', 'transit', 'walking', 'bicycling']:
                    return google_directions(ori, dest, mode)

            else:
                # Default mode is driving
                return google_directions(ori, dest, 'driving')

        else:
            return "Not enough information"

    return 'Formatting Error'

def google_directions(ori, dest, mo):
    
    message = []

    gmaps = googlemaps.Client(key = gmaps_key)
    
    now = datetime.now()
    directions_result = None
    try: 
        directions_result = gmaps.directions(origin=ori, destination=dest, mode=mo, departure_time = now, avoid='tolls')
    
    except:
        return("A network error occurred; please try again")
    
    if directions_result == None:
        return("An error occurred; please check your inputs and try again")
    
    message.append("Start from: " + directions_result[0]['legs'][0]['start_address'])
    message.append("End at: " + directions_result[0]['legs'][0]['end_address'])
    message.append("Duration: " + directions_result[0]['legs'][0]['duration']['text'])
    message.append("Distance: " + directions_result[0]['legs'][0]['distance']['text'])
    
    regex = re.compile('<[^>]*>')
    style_regex = re.compile('<[^>]*(style)[^>]*>')
    for each in directions_result[0]['legs'][0]['steps']:
        instr = re.sub(style_regex, '; ', each['html_instructions'])
        instr = re.sub(regex, '', instr)
        message.append(instr)
        #print(each['html_instructions'])

    return '\n'.join(message)


@app.route("/", methods=['GET', 'POST'])
def process_request():
    """
    Call the Yelp API based off of Twilio responses
    """
    from_number = request.values.get('From')
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "stranger, there was a formatting error in your message, sorry."
        
    bod = request.form.get('Body')

    try:
        if bod != None and 'usage' in bod:
            message = print_usage(bod)
        
        elif bod != None and 'yac' in bod:
            message = process_yelp_and_chill(bod)
            message = "Powered by Yelp\n" + message
        
        elif bod != None and 'random' in bod:
            message = process_random(bod)
            message = "Powered by Yelp\n" + message

        elif bod != None and 'detail' in bod:
            message = process_detail(bod)
            message = "Powered by Yelp\n" + message

        elif bod != None and 'direction' in bod:
            message = process_direction(bod)

        else:
            message = "Incomplete request; more information needed."

    except Exception as e:
        message = "Sorry, there was an error " + str(e)

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
