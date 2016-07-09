#!/usr/bin/python3

from flask import Flask, request, redirect
import twilio.twiml

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
        



    resp = twilio.twiml.Response()
    #resp.sms("SMS Hello Monkey")
    #resp.sms(message)
    resp.message(message)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
