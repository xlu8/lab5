Input = raw_input("enter year: \n")
year = int(Input)
if ((year%100 == 0) and (year%400 == 0)):
       print("%d is leap year.\n"%year)
elif(year % 4 == 0):
       print("%d is leap year. \n"%year)
else:
       print("%d is not leap year. \n"%year)

