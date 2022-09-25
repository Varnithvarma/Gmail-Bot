print ('Welcome to my Bot hope like it')
import time
time.sleep(0.0001)
print('Please Wait')
import smtplib
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login('{your email id}','{your email id password}')
server.sendmail('{sender's email id}',
              '{sender's email id}',
              '{Text you want to send}'
              'thank you')
