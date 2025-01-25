A = {"kitap" :  "book",
     "bilim" : "knowledge",
     "komputer" : "computer"}
key = input("enter the word: ")
if key in A:
    print(key,"-",A[key])
else:
    print("The word isn't in the dictionary")
