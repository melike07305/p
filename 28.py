n = int(input("how many numbers input: "))
jem=0
for i in range(1,n+1):
    a = int(input(f"{i} - number: ")) 
    jem = jem +a
print(f"sum:{jem}")   

#how many numbers input: 5
#1 - number: 18
#2 - number: 81
#3 - number: 63
#4 - number: 99
#5 - number: 94
#sum:355
