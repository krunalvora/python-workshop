students = {"john": 5, "jay": 12, "ricky": 10}

print(students["john"])

students["james"] = 11

print(students)

del students["james"]    # permanent deletion

print(students)

print(students.get("john", "Not available"))
print(students.get("james", "Not available"))
print(students.get("james"))    # Returns None

# Looping through a dictionary

for student, score in students.items():
    print(f"{student} scored {score}")

for student in students:
    print(student)


print("printing all students in alphabetical order: ")
for student in sorted(students):
    print(student)

for score in students.values():
    print(score)
    