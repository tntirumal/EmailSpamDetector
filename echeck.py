import requests
import check as c
import short as s

def validate():
	efile=open("extractlinks.txt","r") #extract file links
	for line in efile.readlines():
		print(line)
		c.checkphish(s.check_short(line))



validate()