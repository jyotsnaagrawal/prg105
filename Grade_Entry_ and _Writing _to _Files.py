def main():
    num_students = int(input("How many students do you enter grades for? "))

    students_list = [['' for _ in range(2)] for _ in range(num_students)]
    for count in range(0, num_students):
        students_list[count][0] =input(f"Enter the name of student{count + 1}: ")
        students_list[count][1] = input("Enter the student's final grade: ").upper()

    print(students_list)

    students_name_grade = open("grades.txt", "w")
    for details in students_list:
        students_name_grade.write("'" + details[0] + "', '" + details[1] + "' \n")
    students_name_grade.close()


main()