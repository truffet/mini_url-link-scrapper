import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

## sample urls or input
#url = input("Enter url:")
url = "http://dr-chuck.com/page1.htm"
#url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

# retrieve html and soup it!
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
anchors = list()
tags = soup.find_all('a')
for tag in tags:
	# tag treated as dict in python
	anchor = tag.get('href', None)
	anchors.append(anchor)

print(anchors)
