# Yelp and Chill
[![Build Status](https://travis-ci.org/YangVincent/yelp-and-chill.svg?branch=vincent)](https://travis-ci.org/YangVincent/yelp-and-chill)
![Heroku](https://heroku-badge.herokuapp.com/?app=yelp-and-chill)

####Overview
Often times, people default to going out to eat or otherwise spending money on a service when they spend time together. This is a tool to help people find places to go and things to do without spending money. 

####Usage Instructions
Currently, the responses are being caught with a heroku server. This won't always work, since it is free. The requirements.txt holds pip3 dependencies needed for heroku. 
Whenever a push is made from this branch, unit tests will be run with Travis CI. If those all pass, it will be deployed on Heroku.
~~Also, heroku gives a key value storage for API keys. This file is the ```.env``` file, and isn't added to git due to the gitignore_global.~~
[Heroku Server](https://yelp-and-chill.herokuapp.com)

During development, only verified numbers can receive messages. These can be checked and modified [here](https://www.twilio.com/user/account/phone-numbers/verified). 
Further information can be found [here](https://www.twilio.com/user/account/log/notifications).

Currently, verified numbers can message `+16503977854` via. SMS. If the message is from a registered number, the response will greet by name. If the message
contains `yac` (yelp and chill), it will give a list of food options around SF. The next step is to give custom locations, or get the location of the sender.

Issues: Yelp doesn't have logic operators, so it is rather difficult to decide what to actually search for. 

Possible alternates: 
1. Put in possible search terms and a number of options and it'll choose for you?
2. Extend yelp functionality for non-smartphone users
3. List popular free options and let them choose - ex: parks, beaches, events, hot air balloons, NOT food items
4. Added extra feature: list restrooms

####Developer Notes
* [Requests](http://docs.python-requests.org/en/master/)
* [Python Yelp](https://github.com/Yelp/yelp-python)
* [Unit Testing](http://docs.python-guide.org/en/latest/writing/tests/)
* [Twilio](https://www.twilio.com/docs/quickstart/python/sms/replying-to-sms-messages)
* [Travel APIs](http://www.programmableweb.com/category/travel/api)
* [Geo Names](http://www.geonames.org/)
* [Deploying Travis then Heroku](http://phansch.net/2014/02/17/travis-heroku-rails/)
* [Travis encrypted environment variables](https://docs.travis-ci.com/user/encrypting-files/)
* [Specific Unit Testing 2](https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html)

####Branches
* `master` - fully functional features
* `vincent` - vincent's development
* `annie` - annie's development

####Features
* Enter location and distance
* Sort by topic/provide topics
* Interface
* Add the ability to send a location (city, zip) via. text and receive a set of suggestions
* Add the ability to search for a type of food (say, Japanese) but filter out items (e.g. not sushi)

