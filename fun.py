import pywhatkit
import time
phonenumber = input("Enter number")
message = input("Enter message")
pywhatkit.sendwhatmsg_instantly(phonenumber, message)
print("Message sent successfully!")
time.sleep(3)
