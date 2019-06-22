#!/bin/python
import random
import argparse
import time
random.seed(time.time())

parser = argparse.ArgumentParser(prog="lk")
group = parser.add_mutually_exclusive_group()

group.add_argument('--sfw', action='store_true', help="randomly print only safe-for-work phrases")
group.add_argument('--nsfw', action='store_true', help="randomly print only not-safe-for-work phrases")

nsfw = ["Fuck you, your life's so fuckin' miserable I ran a 15k to raise \nawareness for it","Get this guy a fucking puppers.",
        "Get this guy a fucking puppers.",
        "Dirty fuckin' dangles, boys!",
        "Fuck Lemony Snicket, what a series of unfortunate events you fuckin' \nbeen through you ugly fuck",
        "You don’t fuck with tradition!",
        "Fuck you Shoresy!",
        "I made your mum so wet, Trudeau deployed a 24-hour infantry unit to \nstack sand bags around my bed!",
        "Pull out the gun, safety's off, fuckin' safety off boys."
        ]

sfw = ["Allegedly...",
          "Pitter-patter, lets get at 'er.",
          "You’re asking the important questions and that’s what I appreciates \nabout you.",
          "Big city slams, boys!",
          "Big city snipes, boys!",
          "Silk mittens, top tittens!",
          "Fore check, back check, pay check, boys!",
          "Ferda.",
          "If you’ve got a problem with her, then you’ve got a problem with me! \nAnd I suggest you let that one marinate!",
          "More hands make less work.",
          "Hard no.",
          "End of the laneway. Don't come up the property.",
          "That’s a Texas-sized 10-4, good buddy!",
          "Great fishin’ in Quebec",
          "Dial that back superchief.",
          "Always bardownski!",
          "Can confirm.",
          "Back to chorin'.",
          "I guess we gots to calls up the internet.",
          "It’s impolite to kiss and tell.",
          "Three things, I hit you, you hit the pavement, ambulance hits 60.",
          "We'll see what you're calling us after I bury a couple of bar-down \nwristers.", 
          "Half-clapper top-cheddar, biscuits top-titties bardownski, always \nbardownski.",
          "A little 3-on-1-ski, a little 3-on-2-ski, home a high hard one? Hit \nthe red light district."
         ]

args = parser.parse_args()

if args.nsfw:
    quoteNum = random.randint(0, len(nsfw) - 1)
    print(nsfw[quoteNum])

elif args.sfw:
    quoteNum = random.randint(0, len(sfw) - 1)
    print(sfw[quoteNum])  

else:
    combined = sfw + nsfw
    quoteNum = random.randint(0, len(combined) - 1)
    print(combined[quoteNum])
     