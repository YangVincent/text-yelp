# Yelp and Chill
[![Build Status](https://travis-ci.org/YangVincent/yelp-and-chill.svg?branch=vincent)](https://travis-ci.org/YangVincent/yelp-and-chill)
![Heroku](https://heroku-badge.herokuapp.com/?app=yelp-and-chill&style=flat)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

[<img src="yelp.png" alt="Powered by Yelp" width="144">](https://www.yelp.com/)
[<img src="google.png" alt="Powered by Google" width="144">](https://www.google.com)

####Overview
Today, 32% of people still don't have smart phones. As such, it is extremely difficult for them to find out about exciting new locations when traveling, or away from the
computer. This allows users to access Yelp through text. 

Additionally, many people have trouble deciding where to go. This helps users randomly decide a user-specified number
of options to choose from, to help eliminate decision fatigue.

As such, there are four main features to this program:

1. Allow non-smartphones to still search for Yelp results, whereas they wouldn't normally be able to
2. Randomly choose an option to combat group indecision when choosing a place to go
3. Find details about results (phone number, address, ratings) 
4. Give directions to an address through different modes of transportation

####Usage Instructions
Currently, verified numbers can message `+16503977854` via. SMS. 
Text `usage` to `+16503977854` to see how to use the application. 

Update: Unfortunately, the Twilio free trial only exists for a limited time. If you would like to see how this application works, please message me at vinyang@ucdavis.edu. Thank you!
~~1. Unfortunately, the Twilio account used is on the free version, but you can sign into [TextFree](textfree.us) to use the registered number `+15302978104`.~~
2. The username and password are both `yelpandchill`. To input newlines as specified in the example from desktop, press `shift+enter`.
For the time being until I can find an application that can receive long messages from Twilio, there are certain constraints. 
3. If you would like to register your number to be verified, feel free to email me. 

`usage` typically texts back

```
Sent from your Twilio trial account - Usage:
1st line is the tool you'd like to use - yac or random
2nd line is the current location (e.g. San Diego)
3rd line is your search string
4th line is the number of random options you'd like to be shown
Here are examples:

yac
San Diego
Escape Room

will return all results for 'Escape Room' in San Diego

random
San Diego
Escape Room
4

will return 4 random results for 'Escape Room' in San Diego
```

To use the TextFree application, I suggest using the `random` option to limit the length of reply. An example would be:

```
random
San Diego
Escape Room
3
```

Next, an example of a response for general `yac` usage with the request:

```
yac
san diego
escape room
```

would be:

```
Sent from your Twilio trial account - Powered by Yelp
Great Room Escape San Diego
Escape Room Police
Ryptic Room Escape
Escapism Puzzle Room
Escape Game SD
The Puzzalarium
Enigma HQ
House of Hints
Divergent Realities
Steal and Escape
The Entrapment
Quicksand Escape Games
3rd Day Escape
Feet First Eventertainment
Escapology
Nate's Point Dog Park - Balboa Park
Balboa Park
Point Loma Sports Club
San Diego Zoo
Kensington Club
```

The user can also ask for details: for the example 
```
detail
San Diego
Balboa Park
```

The reply is
```
Sent from your Twilio trial account - Powered by Yelp

Balboa Park
Phone: +1-619-239-0512
Address: 1549 El Prado
Balboa Park
San Diego, CA 92101
5.0/5 over 1443 reviews
```

Finally, the user can get directions. For example if I am leaving from 
*Sunnyvale Public Library, 665 West Olive Avenue, Sunnyvale, CA 94086*

to 

*Serra park, Tennis Courts, 730 The Dalles Avenue, Sunnyvale, CA 94085* and I want to drive,
I can send:

```
direction
Sunnyvale Public Library, Sunnyvale, CA
Serra Park, Sunnyvale, CA
driving
```

and the response will be
```
Start from: Sunnyvale, CA, USA
End at: Serra park, Tennis Courts, 730 The Dalles Ave, Sunnyvale, CA 94085, USA
Duration: 10 mins
Distance: 3.1 mi
Head east on El Camino Real
Turn right onto E Remington Dr
Turn left onto Hollenbeck Ave
Turn right at Grand Coulee Ave; Destination will be on the right
```

Alternate modes of transportation are ```walking```, ```bicycling```, and ```transit```. Driving is the default mode of transportation.

####Developer Notes
* [Requests](http://docs.python-requests.org/en/master/)
* [Python Yelp](https://github.com/Yelp/yelp-python)
* [Unit Testing](http://docs.python-guide.org/en/latest/writing/tests/)
* [Twilio](https://www.twilio.com/docs/quickstart/python/sms/replying-to-sms-messages)
* [Travel APIs](http://www.programmableweb.com/category/travel/api)
* [Geo Names](http://www.geonames.org/)
* [Deploying Travis then Heroku](http://phansch.net/2014/02/17/travis-heroku-rails/ )
* [Travis encrypted environment variables](https://docs.travis-ci.com/user/encrypting-files/)
* [Specific Unit Testing 2](https://www.twilio.com/blog/2014/03/unit-testing-your-twilio-app-using-pythons-flask-and-nose.html)
* [Google Directions API](https://developers.google.com/maps/documentation/directions/)
* [Google Directions Python API](https://github.com/googlemaps/google-maps-services-python)

####Branches
* `master` - fully functional features
* `vincent` - vincent's development
* `annie` - annie's development

####Features
* Enter location and distance
* Sort by topic/provide topics
* Interface
* Add the ability to send a location (city, zip) via. text and receive a set of suggestions
