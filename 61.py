# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 90
# }

# student_name = input("Student: ")

# if student_name in students:
#     print(f"{student_name}-yň baha: {students[student_name]}")
# else:
#     print(f"{student_name} sözlükde ýok.")
# Charlie-ň baha: 78








scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

iň_uly = max(scores, key=scores.get)
iň_kiçi = min(scores, key=scores.get)

print(f"Iň uly baha: {iň_uly} - {scores[iň_uly]}")
print(f"Iň kiçi baha: {iň_kiçi} - {scores[iň_kiçi]}")
# Iň uly baha: Bob - 92
# Iň kiçi baha: Charlie - 78

