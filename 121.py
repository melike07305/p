import os

for i in range(1,11):
    old_name = str(i)
    new_name = str(i + 90)
    os.rename(old_name,new_name)
    print(f"Folder '{old_name}'ady '{new_name}' adyna uytgedildi")
    
