
from json import load
import smtplib, os
import requests


mysender = "Victorakolo1@gmail.com"
mypassword = "nmswelqppdfnrttd"
Server = smtplib.SMTP('smtp.gmail.com')
Server.starttls()
Server.login(user= mysender, password= mypassword)
Server.sendmail(from_addr= mysender, to_addrs= "victorakolo1@gmail.com", msg= open("weather.py", "w"))

Server.close()
