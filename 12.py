import datetime
isValidDate = False
def checkMessage():
	if(isValidDate) :
		print("Input date is valid ..")
	
	else :
		print("Input date is not valid..")

while isValidDate == False:
	date_entry = input("Enter a date in DD/MM/YYYY format: ")
	day, month, year = map(int, date_entry.split('/'))
	inputDate = datetime.datetime(year, month, day)
	try :
		datetime.datetime(int(year),int(month),int(day))
		isValidDate = True
	except ValueError :
		isValidDate = False
	
	checkMessage()
dateNow = datetime.datetime.now()
duration = inputDate - dateNow
print(duration)
if(month ==2):
	print("meres mina 28")
elif(month%2==0):
	print("meres mina 30")
else:
	print("meres mina 31")

wait=input("press enter")