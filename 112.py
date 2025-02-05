
import os 

while True:
    print("1.Ocurmek\n2.Restart\n3.Buyrugy yzyna almak\n4.chykmak")
    m = int(input("saylan: "))
    if m == 1:
        n = int(input("Nace minutdan: "))
        os.system("shutdown/s/t {n}")
    elif m == 2:
        n = int(input("Nace minutdan: "))
        os.system("shutdown/r/t {n}")
    elif m == 3:
        os.system("shutdown/a")
        print("Buyruk yzyzna alyndy")
    elif m == 4:
        print("Programmany ulananynyz ucin sag bol")
        break



