# Opreators
# Student Details

name = "Supriya"
age = 19
marks = 78
bonus = 5
attendance = 82.5
is_admin = False
is_teacher = False

print("STUDENT DETAILS")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Attendance:", attendance)


# 1. ARITHMETIC OPERATORS

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)


# 2. COMPARISON OPERATORS

print("Equal:", marks == 78)
print("Not Equal:", marks != 50)
print("Greater Than:", marks > 70)


# 3. LOGICAL OPERATORS

is_passed = marks >= 40
has_good_score = marks >= 75

print("AND:", is_passed and has_good_score)
print("OR:", is_admin or is_teacher)
print("NOT:", not is_admin)


# 4. ASSIGNMENT OPERATORS

print("Original Marks:", marks)
marks += bonus
print("After Adding Bonus:", marks)
marks -= 3
print("After Subtracting:", marks)
marks *= 2
print("After Multiplication:", marks)


# FINAL RESULT

print("Student:", name)
print("Final Marks:", marks)
print("Passed:", marks >= 40)
print("Good Score:", marks >= 75)
print("Eligible:", attendance >= 75 and marks >= 40)