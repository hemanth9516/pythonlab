import smtplib
s=smtplib.SMTP('SMPT@MAIL.COM','587')
s.startls()
sender='bathinihemanth977@gmail.com'
reciever='hemanthmadala9500@gmail.com'
msg='hello'
s.login(sender,'******')
s.sendmail(sender,reciver,msg)
print("msg sent succesfully")
s.quit()