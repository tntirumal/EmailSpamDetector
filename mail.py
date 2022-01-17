#modules
import imaplib
import email
import sys


#credentials
#username ="tirumalnanthakumar@gmail.com"

#password
#app_password= "nmarutil2002"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

#login
mail.login(username, app_password)

#select inbox
mail.select("INBOX")

#select specific mails
_, selected_mails = mail.search(None, '(text "www.")')
_, selected_mails1 = mail.search(None, '(text "http")')
_, selected_mails2 = mail.search(None, '(text "bit.ly")')


#open a file to save a body 
file= open(username+'.txt','w')


#total number of mails from specific user
print("Total Messages in www" , len(selected_mails[0].split()))
print("Total Messages in http" , len(selected_mails1[0].split()))
print("Total Messages in bit.ly" , len(selected_mails2[0].split()))



def todecode(a):
    i=0
    for num in a.split():
        i+=1
        
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]
        #print('checking mail %d' %i,end='\r')
        sys.stdout.write("\rchecking mail %d" %i)
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

print("********************www***********************")
print("fetching................")
todecode(selected_mails[0])
print("\n\n\n***************************http***********************")
print("fetching........")
#todecode(selected_mails1[0])
print("\n\n\n*************bit.ly****************")
print("fetching...........")
#todecode(selected_mails2[0])
print("\n\n")
print("##########################COMPLETED..############################")

