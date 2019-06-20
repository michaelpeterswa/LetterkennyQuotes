#!/bin/python
import random
import time
random.seed(time.time())

quotes = ["Fuck you, your lifes so fuckin' miserable I ran a 15k to raise awareness for it",
          "Pitter-patter, lets get at 'er.",
          "You’re asking the important questions and that’s what I appreciates about you.",
          "Get this guy a fucking puppers.",
          "Big city slams, boys!",
          "Big city snipes, boys!",
          "Silk mittens, top tittens!",
          "Fore check, back check, pay check, boys!",
          "Ferda.",
          "If you’ve got a problem with her, then you’ve got a problem with me! And I suggest you let that one marinate!",
          "Dirty fuckin' dangles, boys!",
          "More hands make less work.",
          "Fuck Lemony Snicket, what a series of unfortunate events you fuckin' been through you ugly fuck",
          "Hard no.",
          "End of the laneway. Don't come up the property.",
          "That’s a Texas-sized 10-4, good buddy!",
          "Great fishin’ in Quebec",
          "Dial that back superchief.",
          "You don’t fuck with tradition!",
          "Always bardownski!",
          "Can confirm.",
          "Fuck you Shoresy!",
          "Back to chorin'.",
          "I guess we gots to calls up the internet.",
          "It’s impolite to kiss and tell.",
          "Three things, I hit you, you hit the pavement, ambulance hits 60.",
          "I made your mum so wet, Trudeau deployed a 24-hour infantry unit to stack sand bags around my bed!",
          "We'll see what you're calling us after I bury a couple of bar-down wristers.", 
          "Half-clapper top-cheddar, biscuits top-titties bardownski, always bardownski.",
          "Pull out the gun, safety's off, fuckin safety off boys",
          "A little 3-on-1-ski, a little 3-on-2-ski, home a high hard one? Hit the red light district."]

# for quote in quotes:
#     print(quote)
# print(len(quotes))
# print(random.randint(0, len(quotes) - 1))
quoteNum = random.randint(0, len(quotes) - 1)

print(quotes[quoteNum])