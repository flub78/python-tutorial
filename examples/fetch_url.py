#!/usr/bin/python
# -*- coding:utf8 -*

# a simple script to fecth an HTML page

from urllib.request import urlopen

print ("Fetch url\n")

url = "https://www.quora.com/"
url = "https://vmxeng.atlassian.net/secure/RapidBoard.jspa?rapidView=154&projectKey=SERVERREF&view=reporting&chart=sprintRetrospective&sprint=800"
content = urlopen(url)

print(content.read())

print ("bye")