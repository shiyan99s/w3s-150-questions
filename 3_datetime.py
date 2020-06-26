import datetime
print("Current date and time: ")
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y %H:%m:%S"))