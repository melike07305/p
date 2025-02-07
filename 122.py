import os  
import random

folders = [str(i) for i in range(1,11)]

folders_to_delete = random.sample(folders,8)

for folder in folders_to_delete:
    os.rmdir(folder)
    print(f"Folder '{folder}'pozuldy.")
