# Yelp and Chill
[![Build Status](https://travis-ci.org/YangVincent/yelp-and-chill.svg?branch=vincent)](https://travis-ci.org/YangVincent/yelp-and-chill)
![Heroku](https://heroku-badge.herokuapp.com/?app=yelp-and-chill)

####Overview
Today, 32% of people still don't have smart phones. As such, it is extremely difficult for them to find out about exciting new locations when traveling, or away from the
computer. This allows users to access Yelp through text. Additionally, many people have trouble deciding where to go. This helps users randomly decide a user-specified number
of options to choose from, to help eliminate decision fatigue.

####Usage Instructions
During development, only verified numbers can receive messages. These can be checked and modified [here](https://www.twilio.com/user/account/phone-numbers/verified). 
Further information can be found [here](https://www.twilio.com/user/account/log/notifications).

Currently, verified numbers can message `+16503977854` via. SMS. If the message is from a registered number, the response will greet by name. 
Text `usage` to `+16503977854` to see how to use the application. Unfortunately, the Twilio account used is on the free version, but you can sign into [TextFree](textfree.us)
to use the registered number `+15302978104`. The username and password are both `yelpandchill`. To input newlines as specified in the example from desktop, press `shift+enter`.

####Branches
* `master` - fully functional features
* `vincent` - vincent's development
* `annie` - annie's development

####Features
* Enter location and distance
* Sort by topic/provide topics
* Interface
* Add the ability to send a location (city, zip) via. text and receive a set of suggestions
