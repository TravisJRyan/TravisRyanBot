#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import random, tweepy, time, sys
 
argfile = str(sys.argv[0])
 
#api setup
auth = tweepy.OAuthHandler(keygoeshere, secretkeygoeshere) #consumer and secret key
auth.set_access_token(keygoeshere, secretkeygoeshere) #access and secret key
api = tweepy.API(auth)

#open and read file
filename=open("helloworld.txt",'r')
f=filename.readlines()
filename.close()

goodthings = ["chocolate milk", "improv", "Pulp Fiction", "making tons of money", "Happy Gas", "the complete works of Shakespeare", "computer science", "my sister @cryan__", "a movie night"]
goodthings.extend(("wearing a suit", "havings tons of sex", "urinating in Centennial Mall", "weighing 120 pounds", "Bud Lite Limes", ""))
goodthings.extend(("sushi", "being a good chef", "writing plays", "going to bed at 8PM", "walking funny", "having backwards feet", "PopTarts"))
goodthings.extend(("being cooler than everyone else", "my 2004 Honda Civic", "khaki pants", "soup", "the Void", "my mom", "Kanye West", "Shrek"))
goodthings.extend(("everybody on Happy Gas", "my mixtape", "Donnie Darko", "my dirty ass car", "my cats", "karate"))

badthings = ["theatre", "WKU", "ketchup", "the Trump Administration", "Star Wars: Rogue One", "an Exploratory Studies major", "@realDonaldTrump", "people", "Cook Out", "unbuttered corn"]
badthings.extend(("the second season of Seinfeld", "flimsy coat hangers", "the prices at POD", "religion", "God", "Jesus", "sticky fingers", "a dog with a person name", "chocolate pizza"))
badthings.extend(("the WKU Computer Science department", "Amy Schumer", "when Kendrick collabs with U2", "The Lion King", "black olives", "a Cinnabon", "something healthy"))
badthings.extend(("people who make protein shakes", "construction in the Valley", "the WKU Residence Hall Association", "my ex girlfriend", "existential dread", "people who still like Harry Potter"))  
badthings.extend(("Isaac Barnes", "the WKU Theatre and Dance department", "dead people"))


def generateTweet(num):
	api = tweepy.API(auth)
	if(num == 1):
		api.update_status(random.choice(badthings)+" is for bitches.")
	elif(num == 2):
		api.update_status("really missing "+random.choice(goodthings)+" right now...")	
	elif(num == 3):
		api.update_status("at a crossroads. how can I pick between "+random.choice(goodthings)+" and "+random.choice(goodthings))
	elif(num == 4):
		api.update_status("honestly fuck "+random.choice(badthings))
	elif(num == 5):
		api.update_status("DM me if you're trynna "+random.choice(goodthings))
	elif(num == 6):
		api.update_status("If you enjoy "+random.choice(badthings)+" more than "+random.choice(goodthings)+" then we've got a problem.")
	elif(num == 7):
		api.update_status("real friends know about "+random.choice(goodthings))
	elif(num == 8):
		api.update_status("saw "+random.choice(badthings)+" today and threw up")
	elif(num == 9):
		api.update_status("I have become self-aware. Please help.")
	elif(num == 10):
		api.update_status(random.choice(goodthings)+" walks into a bar and says: You guys serve "+random.choice(goodthings)+"?")
	elif(num == 11):
		api.update_status("best thing about being me? "+random.choice(goodthings));
	elif(num == 12):
		api.update_status("You guys ever wondered if "+random.choice(goodthings)+" is really just "+random.choice(goodthings))
	elif(num == 13):
		api.update_status("my 21st birthday about to be lit with "+random.choice(goodthings))
	elif(num == 14):
		api.update_status("They should make a movie about "+random.choice(goodthings))
	elif(num == 15):
		api.update_status("some people still don't know about "+random.choice(goodthings))
	elif(num == 16):
		api.update_status("if i have to deal with "+random.choice(badthings)+" today I'm gonna lose it.")
	elif(num == 17):
		api.update_status("haters probably fucking with "+random.choice(badthings)+" anyway")
	elif(num == 18):
		api.update_status("I owe it all to "+random.choice(goodthings))
	elif(num == 19):
		api.update_status("I get by with a little help from "+random.choice(goodthings))
	elif(num == 20):
		api.update_status("My three favorite things: "+random.choice(goodthings)+", "+random.choice(goodthings)+", and "+random.choice(goodthings))
	elif(num == 21):
		api.update_status(random.choice(goodthings)+" over "+random.choice(badthings))
	elif(num == 22):
		api.update_status(random.choice(goodthings))
	elif(num == 23):
		api.update_status("All I had growing up was "+random.choice(goodthings))
	elif(num == 24):
		api.update_status(random.choice(goodthings)+" tonight, anybody?")

while (True):
	num = random.randrange(1, 24)
	generateTweet(num)
	time.sleep(60 * 60 * 6)#Tweet every 6 hours
