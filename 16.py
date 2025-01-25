M = input("enter the string: ")
for i in M:
    if i.isupper:
        print(f"{i} - capital letter")
    elif i.islower:
        print(f"{i} - letter")
