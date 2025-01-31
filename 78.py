okuvchylar = {"Nurberdi" : 17,
              "Batyr" : 15,
              "Selim" : 12
}
print(okuvchylar)
okuvchylar["melike"] =  18
okuvchylar["elif"] =  6
okuvchylar["ayperi"] =  20
print(okuvchylar)
okuvchylar["Nurberdi"] = 18
print(okuvchylar)
okuvchylar.pop("Batyr")
print(okuvchylar)
for i in okuvchylar:
    print(i)
for a in okuvchylar:
    print(okuvchylar[a])

#{'Nurberdi': 17, 'Batyr': 15, 'Selim': 12}
#{'Nurberdi': 17, 'Batyr': 15, 'Selim': 12, 'melike': 18, 'elif': 6, 'ayperi': 20}       
#{'Nurberdi': 18, 'Batyr': 15, 'Selim': 12, 'melike': 18, 'elif': 6, 'ayperi': 20}       
#{'Nurberdi': 18, 'Selim': 12, 'melike': 18, 'elif': 6, 'ayperi': 20}
#Nurberdi
#Selim
#melike
#elif
#ayperi
#18
#12
#18
#6
#20
