import os 
num = int(input("Nace sany folder doretmekci: "))

for i in range(1,n+1):
    ady = input("Folder ady: ")
    os.mkdir(f"{ady}")
