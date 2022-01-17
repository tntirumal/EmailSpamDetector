# Program to make a simple
# login screen


import tkinter as tk
import imaplib
import email
import sys,os
import check as c
import short as s

c.cyan("e-mail spam detector")
c.cyan("######## DEVELOPED BY TIRUMAL ###########")

root=tk.Tk()

# setting the windows size
root.geometry("600x400")
root.configure(background='yellow')
root.title("EMAIL SPAM DETECTOR (ESD)")
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen




def submit():

	name=name_var.get()
	password=passw_var.get()
	
	print("The name is : " + name)
	print("The password is : " + len(password)*'*')
	
	connect(name,password)
	extract(name)
	validate()

	name_var.set("")
	passw_var.set("")

	return name,password


	
def connect(name,password):
	def todecode(a):
	    i=0
	    for num in a.split():
	        i+=1
	        
	        _, data = mail.fetch(num , '(RFC822)')
	        _, bytes_data = data[0]
	        #print('checking mail %d' %i,end='\r')
	        sys.stdout.write("\rchecking mail contents %d" %i)
	        sys.stdout.flush()


	        #convert the byte data to message
	        email_message = email.message_from_bytes(bytes_data)
	        #print("\n===========================================")


	        #access data
	        #print("Subject: ",email_message["subject"])
	        '''print("To:", email_message["to"])
	        print("From: ",email_message["from"])
	        print("Date: ",email_message["date"])'''
	        for part in email_message.walk():
	            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
	                try:
	                    message = part.get_payload(decode=True)
	                    #print("Message: \n", message.decode())
	                    file.write(message.decode())
	                    

	                    
	                except Exception  as e:
	                    
	                    continue
	                
	                
	                #print("==========================================\n")
	                break


	try:
		# https://www.systoolsgroup.com/imap/
		gmail_host= 'imap.gmail.com'
		yahoo_host='imap.mail.yahoo.com'

		#set connection
		if '@gmail.com' in name:
			mail = imaplib.IMAP4_SSL(gmail_host)
		elif '@yahoo.com' in name:
			mail = imaplib.IMAP4_SSL(yahoo_host)
		else:
			print("UNKNOWN HOST...contact developer")
			exit(0)

		#login
		mail.login(name, password)

		#select inbox
		mail.select("INBOX")
		print("successfully connected to mail...")
		print("\n NOW FETCHING...\n")

		file= open(name+'.txt','w')
		_, selected_mails = mail.search(None, '(text "www.")')
		_, selected_mails1 = mail.search(None, '(text "http")')
		_, selected_mails2 = mail.search(None, '(text "bit.ly")')
		_, selected_mails2 = mail.search(None, '(text "https")')


		#total number of mails from specific user
		print("Total Messages in www" , len(selected_mails[0].split()))
		print("Total Messages in http" , len(selected_mails1[0].split()))
		print("Total Messages in bit.ly" , len(selected_mails2[0].split()))


		print("********************www***********************")
		print("fetching................")
		todecode(selected_mails[0])
		print("\n\n\n***************************http***********************")
		print("fetching........")
		todecode(selected_mails1[0])
		print("\n\n\n*************bit.ly****************")
		print("fetching...........")
		todecode(selected_mails2[0])
		print("\n\n")
		print("##########################COMPLETED..############################")
		




	
	except Exception as e:
		raise e
		

def extract(name):
	import re
	file2=open('extractlinks.txt','w')
	print("extracting links..."+"\n")
	with open(name+".txt") as file:
		for line in file:
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
			#print("Original string: ",line)
			if not urls:
				pass
			else:

				for i in urls:
					i.replace('>',"")
					
					file2.write(i+"\n")

	file2.close()


def validate():
	efile=open("extractlinks.txt","r") #extract file links
	for line in efile.readlines():
		print(line)
		c.checkphish(s.check_short(line))

	print("============COMPLETED============")





# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

exit_btn=tk.Button(root,text='exit',command=exit,bg='red')


# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
exit_btn.grid(row=2,column=2)
# performing an infinite loop
# for the window to display
root.mainloop()
