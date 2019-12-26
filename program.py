# Reading Content

import csv

QuoteFile = open('./Email_Quotes/QuoteList.csv') # https://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/#13cea60f6c7a
QuoteReader = csv.reader(QuoteFile)
quotelist = list(QuoteReader)

RecipeientFile=open('./Email_Quotes/Email_list.csv')
RecipeientReader = csv.reader(RecipeientFile)
recipeientlist = list(RecipeientReader)

#Scheduling

i=int(list(csv.reader(open('./Email_Quotes/iterator.csv')))[0][0])
iteratorfile = open('./Email_Quotes/iterator.csv', 'w', newline='')
iteratorWriter = csv.writer(iteratorfile)
iteratorWriter.writerow([i+1])
iteratorfile.close()

#Sending Mail

"""
Login
Send Mail
Quit
#
"""

import smtplib
domain_name='smtp.gmail.com'
port=587
smtpObj = smtplib.SMTP(domain_name,port)
#smtpObj.ehlo()
smtpObj.starttls() # Enables Encryption

sender_mail_id='[***]@gmail.com'
sender_password='***'

smtpObj.login(sender_mail_id, sender_password) # Might require application specific password or allow access to less secure apps


subject='Quote of the Day'
subject='Subject:'+ subject + '\n'
content=quotelist[i][0]
mail_body=(subject+content)
#for email_id in recipeientlist:
#    recipientemailid=email_id
smtpObj.sendmail(sender_mail_id, recipeientlist, mail_body.encode()) 

smtpObj.quit()
