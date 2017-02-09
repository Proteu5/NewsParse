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

# Menu system!
def menu():
	strs = ("1. Reuters: World News\n"
        	"2. Reuters: Technology News\n"
        	"3. Reuters: Business News\n"
        	"4. Open URL\n"
        	"5. Exit : ")
	choice = input(strs)
	return int(choice) 

def url():
	choice_2 = input()
	webbrowser.open(choice_2)

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
    	print ("Enter a URL: ") 
    	url()
    elif choice == 5:
        break


