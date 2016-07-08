# Yelp and Chill

####Overview
Often times, people default to going out to eat or otherwise spending money on a service when they spend time together. This is a tool to help people find places to go and things to do without spending money. 

####Usage Instructions
Currently, the responses are being caught with a heroku server. This won't always work, since it is free. The requirements.txt holds pip3 dependencies needed for heroku. 
Also, heroku gives a key value storage for API keys. This file is the ```.env``` file, and isn't added to git due to the gitignore_global. 
[Heroku Server](https://yelp-and-chill.herokuapp.com)

####Developer Notes
* [Requests](http://docs.python-requests.org/en/master/)
* [Python Yelp](https://github.com/Yelp/yelp-python)
* [Unit Testing](http://docs.python-guide.org/en/latest/writing/tests/)
* [Twilio](https://www.twilio.com/docs/quickstart/python/sms/replying-to-sms-messages)
* [Travel APIs](http://www.programmableweb.com/category/travel/api)
* [Geo Names](http://www.geonames.org/)
 
####Branches
* `master` - fully functional features
* `vincent` - vincent's development
* `annie` - annie's development

####Features
* Enter location and distance
* Sort by topic/provide topics
* Interface
* Add the ability to send a location (city, zip) via. text and receive a set of suggestions
