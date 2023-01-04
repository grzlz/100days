# Write a program than converts their scores to grades. 
# Score 91-100, Outstanding
# 81-90 "Exceeds expectations"
# 71-80 "Acceptable
#  70 < Fail

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    grade = ""
    if student_scores[key] < 70:
        grade = "Fail"

    elif student_scores[key] <= 80:
        grade = "Acceptable"

    elif student_scores[key] <= 90:
        grade = "EX"

    else:
        grade = "Outstanding"
    
    student_grades[key] = grade

print(student_grades)