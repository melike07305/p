import  datetime
sagat = int(input("Enter the number of hour? "))
T = datetime.datetime.today()
H = datetime.timedelta(hours = sagat)
R = T + H
print("date after", sagat, "hours: ",R.strfrtime('%d.%m.%Y %X'))
