"""
num = 7
while (num < 10):
    print("Connection problem tonight")
    num = num+1
print("simple while example")
print("*" * 60)
keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Enter the sales value: "))
    commision = (float(input("Enter your commission: ")))
    commision = commision/100
    actual_amount = sales * commision
    print (f"Your commisson is  {actual_amount: .2f}")
    keep_going = input("Do you want to continue another commission - type y for yes: ")
print("Thank you for using my repetition program")

print ("*" * 60)
for n in range(5):
    #print(n)
    print(n, "We wasted almost 40 minutes tonight with technical problems")
print ('Thank you for using my for repetition loop')
print ("*" * 60)
# for loop with a string acting as a range
for letter in ("Anindya"):
    print(letter)
print ('Thank you for using my for repetition loop')
print ("*" * 60)
# for loop with two parameters
for val in range (1, 5):
    print (val, "Hello")
print("Thank you for using the two parameter loop")
print ("#" * 60)
# for loop with three parameters
for a in range (10, 100, 10):
    print ("Values are: ", a)
print("Thank you for using my three parameter loop")
print ("*" * 60)
print(f'number {"square": >8}')

for i in range(6):
    print (f'{i:>6}{i ** 2:>8}')
print("Thank you for using my square program")
3 """

''''
sender = "Victorakolo1@gmail.com"
password = "victor7521"
receiver = "Vakolo@stetson.edu"
subject = "Weather Report"
email_body = firstfunc()


email_text = """\

From: %s

To: %s

Subject: %s



%s

""" % (sender, ", ".join(receiver), subject, email_body)

try:

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    smtp_server.ehlo()

    smtp_server.login(sender, password)

    smtp_server.sendmail(sender, receiver, email_text)

    smtp_server.close()

    print ("Email sent successfully!")

except Exception as ex:

    print("Something went wrong….",ex)
    '''