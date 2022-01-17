import requests

def red(skk): print("\033[91m {}\033[00m" .format(skk))

def green(skk): print("\033[92m {}\033[00m" .format(skk))

def yellow(skk): print("\033[93m {}\033[00m" .format(skk))

def lightpurple(skk): print("\033[94m {}\033[00m" .format(skk))

def purple(skk): print("\033[95m {}\033[00m" .format(skk))

def cyan(skk): print("\033[96m {}\033[00m" .format(skk))

def lightgray(skk): print("\033[97m {}\033[00m" .format(skk))

def black(skk): print("\033[98m {}\033[00m" .format(skk))

def check_short(lurl):
	if "http" in lurl:
		pass
	else:
		lurl="https://"+lurl
	url=lurl
	try:
		res=requests.get(lurl,allow_redirects=False,verify=False)
		print(res)
		if(res.status_code==301 ):
			red("Found a redirection")
			#print(res.headers['Location'])

			url=res.headers['Location']
			#print("please save the above link")
		elif(res.status_code==200):
			yellow("no redirection found..This is original link")
			#print(url)
			#url=lurl
		else:
			cyan("response returns "+str(res.status_code))

	
	except Exception as e:
		red("warning phishing site.connection could not established")
		pass


	return url

#print(check_short('https://www.quora.com/qemail/track_click?aoid=dioMVNc4rZ8&aoty=4&aty=4&cp=0&ct=1634007725963106&et=146&id=b8833b2f00bb44a9be548397404154c2&notif_type=418&request_id=418&snid=27430993565&src=1&st=1634007725971186&stories=%5B(%3Cstory_types.tribe_post%3A+10%3E%2C+39771555)%2C+(%3Cstory_types.tribe_post%3A+10%3E%2C+39304606)%2C+(%3Cstory_types.tribe_post%3A+10%3E%2C+39989249)%5D&tribe_item_ids=qFRpZ3wgbcU%7CI6ggxAMBFBB%7C4mDSEY2Npy&uid=30uLNzi8vPF&v=0'))