import  datetime
gun = int(input("Enter the number of days? "))
T = datetime.datetime.today()
D = datetime.timedelta(days = gun)
R = T - D
print("days before", gun, "days: ",R.strfrtime('%d.%m.%Y'))
