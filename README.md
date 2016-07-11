# Yelp and Chill
[![Build Status](https://travis-ci.org/YangVincent/yelp-and-chill.svg?branch=vincent)](https://travis-ci.org/YangVincent/yelp-and-chill)
![Heroku](https://heroku-badge.herokuapp.com/?app=yelp-and-chill)

####Overview
Today, 32% of people still don't have smart phones. As such, it is extremely difficult for them to find out about exciting new locations when traveling, or away from the
computer. This allows users to access Yelp through text. 

Additionally, many people have trouble deciding where to go. This helps users randomly decide a user-specified number
of options to choose from, to help eliminate decision fatigue.

As such, there are two main features to this program:

1. Allow non-smartphones to still search for Yelp results, whereas they wouldn't normally be able to
2. Randomly choose an option to combat group indecision when choosing a place to go

####Usage Instructions
During development, only verified numbers can receive messages. These can be checked and modified [here](https://www.twilio.com/user/account/phone-numbers/verified). 
Further information can be found [here](https://www.twilio.com/user/account/log/notifications).

Currently, verified numbers can message `+16503977854` via. SMS. If the message is from a registered number, the response will greet by name. 
Text `usage` to `+16503977854` to see how to use the application. 

1. Unfortunately, the Twilio account used is on the free version, but you can sign into [TextFree](textfree.us) to use the registered number `+15302978104`. 
2. The username and password are both `yelpandchill`. To input newlines as specified in the example from desktop, press `shift+enter`.
For the time being until I can find an application that can receive long messages from Twilio, there are certain constraints. 

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
Sent from your Twilio trial account - Great Room Escape San Diego
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

####Branches
* `master` - fully functional features
* `vincent` - vincent's development
* `annie` - annie's development

####Features
* Enter location and distance
* Sort by topic/provide topics
* Interface
* Add the ability to send a location (city, zip) via. text and receive a set of suggestions
