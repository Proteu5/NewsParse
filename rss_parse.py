import feedparser

d=feedparser.parse('http://feeds.reuters.com/Reuters/worldNews')

for post in d.entries:
	print (post.title+ ":"+post.link+"\n")


