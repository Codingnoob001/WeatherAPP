
import smtplib, os
import requests

def weatherfunc(city = "Deland", myAPI_key="83638b5c9cd924922907b2743a72924d", URL="http://api.openweathermap.org/data/2.5/weather"):
     url_request = "{}?appid={}&q={}".format(URL, myAPI_key, city) 
     feedback = requests.get(url_request)
     if feedback.status_code == 200:
            weather_values = feedback.json()
            weather = weather_values['weather'][0]['description'] 
            temperature = round(weather_values["main"]["temp"]-273.15, 2) 
            max_temp = round(weather_values["main"]["temp_max"]-273.15, 2) 
            lowest_temp = round(weather_values["main"]["temp_min"]-273.15, 2)
            print("Weather:", weather, "\nCurrent temperature:", temperature, "Celsius", "\nMaximum day Temperature:", max_temp, "celsius", "\nMinimum day temperature:", lowest_temp, "celsius" )
            if max_temp >= 30 or temperature > 30:
               print("Today will get hot during the day, wear something Light")
            elif 23 < temperature or lowest_temp < 20:
               print("Today's temperature will same as room temperature; dress as you wish :)")
            else:
               print("Today will be cold; suit up!")
     else:
            print("Something is wrong :")

       
     return {"Weather": weather, "Current temperature": temperature, "Maximum day Temperature": max_temp, "Minimum day temperature": lowest_temp}


text = weatherfunc()
sender = "From: Victorakolo1@gmail.com"
mailing_list = ["vakolo@stetson.edu", "victorakolo11@gmail.com"]
mypassword = "nmswelqppdfnrttd"
Server = smtplib.SMTP('smtp.gmail.com')
Server.starttls()
subject = "Today's Weather Report"
body = "Hi, Friend.\n\nBelow is today's weather report: "
farewell = "Have a good day!"
message ='Subject: {0}\n\n{2}\n\n{1}\n\n\n{3}'.format(subject, text, body, farewell)
Server.login(user= sender, password= mypassword)
Server.sendmail(from_addr= sender,  to_addrs= mailing_list, msg= message)

Server.close()
