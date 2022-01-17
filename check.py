import short as  s
import requests

fp=open('harmlink.txt','a')

def red(skk): print("\033[91m {}\033[00m" .format(skk))

def green(skk): print("\033[92m {}\033[00m" .format(skk))

def yellow(skk): print("\033[93m {}\033[00m" .format(skk))

def lightpurple(skk): print("\033[94m {}\033[00m" .format(skk))

def purple(skk): print("\033[95m {}\033[00m" .format(skk))

def cyan(skk): print("\033[96m {}\033[00m" .format(skk))

def lightgray(skk): print("\033[97m {}\033[00m" .format(skk))

def black(skk): print("\033[98m {}\033[00m" .format(skk))




#check_short(url)
#url=input("please the type the url that is shown above: ")

def checkphish(url):

	if "http" in url:
		pass
	else:
		url="https://"+url

	if "cloudflare" in url:
		red("i can't detect for phishing site in cloudflare launched website")
		yellow("Because cloudflare is hosting a original site which can provide on running javascript")
		purple("sorry my detection might be wrong ... i'm exiting now")
		exit(0)
	html_output_name ="test"
	try:
		req = requests.get(url, 'html.parser')
	except requests.exceptions.SSLError:
		lightpurple("there occurred an ssl verify error")
		yellow("do you this site and do you wish to continue")
		choice=input("To continue press 0  or you doesn't aware of this site press 1: ")
		if(choice == '0'):
			red("seeing in your own risk")
			yellow("my suggestion is not to give any personal details...unless you know this host personally")
			lightpurple("BECAUSE THIS IS NOT SSL VERIFIED")
			req = requests.get(url,'html.parser',verify=False)
		else:
			purple("ok...now i'm exiting..")
			#exit(0)
			pass
	except Exception:
		cyan("error occured please check does the website is hosted")
		fp.write(url)
		yellow("MY ADVICE IS TO DELETE THE MAIL WHICH CONTAINS THE BELOW LINK")
		purple(url)
		exit(0)
	#html_output_name=input("enter the file name")
	with open(html_output_name, 'a') as f:
	    f.write(req.text)
	    f.close()






	#the program to find for a wordin python
	word_list=['True','False','src','rsrc.php','true','false','function','%']
	word_list_phish=['action','.php','login.php','.html']
	#html_output_name=input("enter file name")
	word_list_captured=[]
	word_list_captured_phish=[]

	with open(html_output_name,'r') as f:
	    file_content = f.read()

	for x in word_list:
	    if x in file_content:
	        word_list_captured.append(x)

	if(len(word_list_captured)<2):
		for x in word_list:
		    if x in file_content:
		        word_list_captured_phish.append(x)

	if(len(word_list_captured)>len(word_list_captured_phish)):
		green("there is a no chances of phishing...")
	else:
		red("there is a chances of phishing")
		
		fp.write(url)
		print(url)



