students = ["Summer", "Jacob", "Rachael"]

print(students[0])
print(students[1])
print(students[2])

#OR

for student in students:
    print(student)

#OR

for i in range(len(students)):
    print(students[i])

#OR

#note: Associate each name with a favorite number
favorite_numbers = {
    "Rachael": 7,
    "Jacob": 13,
    "Summer": 4
}

print(favorite_numbers["Jacob"])  #note: Output: 13
