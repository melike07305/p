N = int(input("how many students: "))
student = []
for i in range(1,N+1):
    name = input(f"{i}- Name: ")
    student.append(name)
print(student)
