#!/usr/bin/python3

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """ respond to incoming calls with a simple text message. """

    #resp = twilio.twiml.Response()
    #resp.message = ("Hello, Mobile Monkey")
    #return str(resp)

    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
