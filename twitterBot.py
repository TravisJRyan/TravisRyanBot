#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import random, tweepy, time, sys
 
#api setup
auth = tweepy.OAuthHandler("UWmfn8JDmCUAM78xSIfveAUFt", "eEvkGQm1nSsiT5iJjG4SCyubUyRVtN2cDYKguUfvDYuR0omDDI") #consumer and secret key
auth.set_access_token("863590434425196548-B8zgCMW1iUPFXbSqSjC9AufHnKwcywp", "mkc4V8LmNT8SdLJIZBpxKbGX7LAF4qp2f0knMdC2TCwT4") #access and secret key
api = tweepy.API(auth)
 
#list of good things
goodthings = {1: "chocolate milk", 2: "improv", 3: "Pulp Fiction", 4: "making tons of money", 5: "Happy Gas", 6: "the complete works of Shakespeare", 7: "computer science", 8: "my sister @cryan__", 9: "a movie night", 10: "wearing a suit", 11: "havings tons of sex", 12: "urinating in Centennial Mall", 13: "weighing 120 pounds", 14: "Bud Lite Limes", 15: "sushi", 16:"being a good chef", 17: "writing plays", 18: "going to bed at 8PM", 19: "walking funny", 20: "having backwards feet", 21: "PopTarts", 22: "being cooler than everyone else", 23: "my 2004 Honda Civic", 24: "khaki pants", 25: "soup", 26: "the Void", 27: "my mom", 28: "Kanye West", 29: "Shrek", 30: "everybody on Happy Gas", 31: "my mixtape", 32: "Donnie Darko", 33: "my dirty ass car", 34: "my cats", 35: "karate", 36: "fast cars", 37: "Albert Camus", 38: "Michael Keaton", 39: "chocolate milk"}
 
#list of bad things
badthings = {1: "theatre", 2: "WKU", 3: "ketchup", 4: "the Trump Administration", 5: "Star Wars: Rogue One", 6: "an Exploratory Studies major", 7: "@realDonaldTrump", 8: "people", 9: "Cook Out", 10: "unbuttered corn", 11: "the second season of Seinfeld", 12: "flimsy coat hangers", 13: "the prices at POD", 14: "religion", 15: "God", 16: "Jesus", 17: "sticky fingers", 18: "a dog with a person name", 19: "chocolate pizza", 20: "the WKU Computer Science department", 21: "Amy Schumer", 22: "when Kendrick collabs with U2", 23: "The Lion King", 24: "black olives", 25: "a Cinnabon", 26: "people who make protein shakes", 27: "construction in the Valley", 28: "the WKU Residence Hall Association", 29: "my ex girlfriend", 30: "existential dread", 31: "people who still like Harry Potter", 32: "dead people", 33: "musical theatre", 34: "Steve Bannon", 35: "ducks", 36: "Bowling Green", 37: "milk that isn't chocolate", 38: "vegetables", 39: "when people cramp my style"}
 
#array of used terms
used = []
 
def buildTweetLoop():
  mycondition = True
  while(mycondition):
    goodorbad = random.randrange(1,3) #generate "good or bad thing" tweet
    choice = random.randrange(1, 39)
    print(goodorbad) #generate 1-39 for the specific good or bad thing
    if (goodorbad == 1) and (not goodthings[choice] in used):
 	finishGoodTweet(goodthings[choice])
	used.extend(goodthings[choice])
	mycondition = False
    elif (goodorbad == 2) and (not badthings[choice] in used): #if unused 	
	finishBadTweet(badthings[choice])
	used.extend(badthings[choice])
	mycondition = False
 
def finishGoodTweet(phrase):
  num = random.randrange(1,20)
  othernum = random.randrange(1,39)
  if(num == 1):
    final = "It's not summer without "+phrase
  elif(num == 2):
    final = "I get by with a little help from "+phrase
  elif(num == 3):
    final = "has anyone seen "+phrase
  elif(num == 4):
    final = "only real friends know about "+phrase
  elif(num == 5):
    final = "who needs religion when you have "+phrase
  elif(num == 6):	
    final = "things haven't been the same without "+phrase
  elif(num == 7):
    final = "I predict a bad thing happening to "+phrase
  elif(num == 8):
    final = "man i sure do love "+phrase
  elif(num == 9):
    final = "where my "+phrase+" at?"
  elif(num == 10):
    final = "I traded "+phrase+" for "+goodthings[othernum]
  elif(num == 11):
    final = "only thing I love more than "+phrase+" is "+goodthings[othernum]
  elif(num == 12):
    final = "how do people live without "+phrase
  elif(num == 13):
    final = phrase+" is better than "+badthings[othernum]
  elif(num == 14):
    final = "people who are into "+badthings[othernum]+" should try "+phrase+" instead"
  elif(num == 15):
    final = "What is my purpose?"
  elif(num == 16):
    final = "really missing "+phrase
  elif(num == 17):
    final = "anybody up for "+phrase+" later?"
  elif(num == 18):
    final = phrase+" is underrated"
  elif(num == 19):
    final = "shoutout to "+phrase
  elif(num == 20):
    final = "haters don't even know about "+phrase
  api.update_status(final)
 
def finishBadTweet(phrase):
  num = random.randrange(1,20)
  othernum = random.randrange(1,39)
  if(num == 1):
    final = "hoping one day i won't have to deal with "+phrase
  elif(num == 2):
    final = "nothing worse than "+phrase
  elif(num == 3):
    final = "i really don't like "+phrase
  elif(num == 4):
    final = "anybody got my back in this "+phrase+" situation?"
  elif(num == 5):
    final = "smh "+phrase
  elif(num == 6):	
    final = "nobody should have to deal with "+phrase
  elif(num == 7):
    final = "worst thing that happened to me today? "+phrase
  elif(num == 8):
    final = "2 worst things in my life: "+phrase+" and "+badthings[othernum]
  elif(num == 9):
    final = "ugh. "+phrase
  elif(num == 10):
    final = "Managed to get rid of "+phrase+" in exchange for "+goodthings[othernum]
  elif(num == 11):
    final = "only thing I hate more than "+phrase+" is "+badthings[othernum]
  elif(num == 12):
    final = "is there anyone that likes "+phrase
  elif(num == 13):
    final = phrase+" or "+badthings[othernum]+"?"
  elif(num == 14):
    final =  phrase+"? Lame..."
  elif(num == 15):
    final = "Help me. I have become self-aware."
  elif(num == 16):
    final = "Awwww man it's "+phrase
  elif(num == 17):
    final = "Really getting tired of "+phrase
  elif(num == 18):
    final = phrase+" is overrated"
  elif(num == 19):
    final = "you guys ever wonder where "+phrase+" came from?"
  elif(num == 20):
    final = "get "+phrase+" away from me"
  api.update_status(final)
 
while (True):
	buildTweetLoop()
	time.sleep(60 * 60 * 6)#Tweet every 6 hours
 
