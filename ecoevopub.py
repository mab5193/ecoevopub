curl 'https://www.eeb.ucla.edu/seminars.php?id=[001-800]'> [1-800].html

from bs4 import BeautifulSoup
import os, os.path
seminarlist= os.listdir("seminars")
for seminar in seminarlist:
	soup= BeautifulSoup(open("seminars/"+seminar))
	name_pane=soup.find(class_="section")
	date=name_pane.find("h4")
	name=name_pane.find("p")
	print date.string, name.string


