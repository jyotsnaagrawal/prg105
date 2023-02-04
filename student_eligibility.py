# Directions :-You are writing a program to determine if a student is eligible for financial aid for the next semester.
# To qualify, the student must either be a new student or a current student with a GPA of 2.0 or higher.
# Additionally, the student may not have a criminal record for drugs,
# must enroll in a minimum of six credit hours of classes, and must have a gross yearly income of less than $50,000.
# You will gather information from the student, and you will let them know if they are eligible
# for financial aid or not.
# This test for in-eligibility for financial aid.
print(" This Program for in- eligibility of students to apply for financial aid \n ")

student_status = input(" Are you a new student or returning student. Pleases enter r or n: ")
gpa = 0.0
if student_status == "r":
    gpa = float(input(" What is your current GPA? "))

felony = input(" Have you ever been convicted of a drug felony ? (enter y or n): ")
credit_hours = int(input(" How many credit hours are you enrolled for next semester? "))
income = int(input(" What is your gross yearly income, rounded to the nearest dollar? Don't use commas. "))

if (student_status == "r" and gpa < 2.0) or (felony == "y") or (credit_hours < 6) or (income >= 50000):
    print(" You are not eligible to apply  for financial aid.")
else:
    print(" You are eligible to apply for financial aid.")
