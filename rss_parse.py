### RSS Feed Reader ###
#!/usr/bin/env python

"""rss_parse.py: Parse RSS Feeds."""
__author__ = "Proteu5"
__copyright__ = "Copyright 2017, The Enigma Project"
__credits__ = ["Proteu5"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Proteu5"
__email__ = "null@gmail.com"
__status__ = "In Production"

import feedparser
import webbrowser
import sys


# Menu system!
def menu():
	strs = ("1. Reuters: World News\n"
        	"2. Reuters: Technology News\n"
        	"3. Reuters: Business News\n"
        	"4. Reuters: Egypt \n"
        	"5. Open URL\n"
        	"6. Clipboard\n"
        	"7. Exit : ")
	choice = input(strs)
	return int(choice) 

def menu_io():
	strs_2 = ("1. Write\n"
        	"2. Read\n"
        	"3. URL\n"
        	"4. Exit : ")
	choice_io = input(strs_2)
	return int(choice_io) 

def url():
	choice_2 = input()
	webbrowser.open(choice_2)

def clip():
	while True:
		choice_io = menu_io()
		if choice_io == 1:
			choice_3 = input()
			f=open("links","a+")
			f.write(choice_3+"\n")
			f.close
		elif choice_io == 2:
			print ("Read")
			f=open("links","r")
			if f.mode == 'r':
				contents =f.read()
				print (contents)
		elif choice_io == 3:
			print ("Enter a URL: ")
			url()	
		elif choice_io == 4:
			break


while True:
    choice = menu()
    if choice == 1:
      print ("Reuters World News")
      d=feedparser.parse('http://feeds.reuters.com/Reuters/worldNews')
      for post in d.entries:
	      print (post.title+ ":"+post.link+"\n")
    elif choice == 2:
      print ("Reuters Technology News")
      d=feedparser.parse('http://feeds.reuters.com/reuters/technologyNews')
      for post in d.entries:
	      print (post.title+ ":"+post.link+"\n")
    elif choice == 3:
      print ("Reuters Business News") 
      d=feedparser.parse('http://feeds.reuters.com/reuters/businessNews')
      for post in d.entries:
	      print (post.title+ ":"+post.link+"\n")
    elif choice == 4:
      print ("Egypt Headlines") 
      d=feedparser.parse('http://feeds.reuters.com/reuters/AFRICAegyptNews')
      for post in d.entries:
	      print (post.title+ ":"+post.link+"\n")
    elif choice == 5:
    	print ("Enter a URL: ") 
    	url()
    elif choice == 6:
    	print ("Clipboard: ")
    	clip()
    elif choice == 7:
        break


