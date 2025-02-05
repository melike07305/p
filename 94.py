import os 

A = os.listdir()
for i in A:
    if i.endswith("docx"):
    print(i)
