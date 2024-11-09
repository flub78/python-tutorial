#!/usr/bin/python
# -*- coding:utf8 -*


print ("dict of dict\n")

students = {
    "student1": {
        "name": "Alice",
        "age": 21,
        "major": "Physics"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "major": "Mathematics"
    },
    "student3": {
        "name": "Charlie",
        "age": 20,
        "major": "Biology"
    }
}

# Accessing the name of student1
student1_name = students["student1"]["name"]
print(f"Student 1 Name: {student1_name}")

# Accessing the age of student2
student2_age = students["student2"]["age"]
print(f"Student 2 Age: {student2_age}")

# Accessing the major of student3
student3_major = students["student3"]["major"]
print(f"Student 3 Major: {student3_major}")

# Updating student1's age
students["student1"]["age"] = 23

# Adding a new field to student2
students["student2"]["graduation_year"] = 2023

# Printing the updated dictionary
print(students)

for student in students.values():
    print(student)