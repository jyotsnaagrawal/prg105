def main():
    numbers_dict = {"un": "one", "deux": "two", "trois": "three", "quatre": "four", "cinq": "five",
                    "six": "six", "sept": "seven", "huit": "eight", "neuf": "nine", "dix": "ten"}
    print("Enter the number in English which corresponds to the number in french. ")
    keys = list(numbers_dict.keys())
    score = 0
    total = 10
    grade = 0
    for key in keys:
        answer = input(f"What is the equivalent of {key} :")
        if answer.lower() == numbers_dict[key].lower():

            print("Correct")
            score += 1
        else:
            print("Incorrect. The correct answer is", numbers_dict[key])
            if score >= 9:
                grade = "A"
            elif score>= 8:
                grade = "B"
            elif score >= 7:
                grade = "C"
            elif score >= 6:
                grade = "D"
            else:
                grade = "F"
    print(f"Your final score is {score}/{total} ")
    print(grade)


main()
