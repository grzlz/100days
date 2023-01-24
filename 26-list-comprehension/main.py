from random import randint
# dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_dict = {name: randint(1, 100) for name in names}
print(students_dict)

# Create passed students dict

passed_students = {name:grade for (name, grade) in students_dict.items() if grade > 50}
print(passed_students)