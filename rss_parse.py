import feedparser

# Menu system!
def menu():
	strs = ("1. Reuters: World News\n"
        	"2. Reuters: Technology News\n"
        	"3. Reuters: Business News\n"
        	"4. Exit : ")
	choice = input(strs)
	return int(choice) 

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
        break
 
#for post in d.entries:
#	print (post.title+ ":"+post.link+"\n")


