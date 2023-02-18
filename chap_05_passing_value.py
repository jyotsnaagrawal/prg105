# Create a program that asks a user to enter a whole number between 20 and 100.  Send that number to a function that
# will validate the number, and if it is not a number between 20 and 100, use a while loop to keep asking the user
# for a valid number. Return the number to the main function.
# In addition, create three functions that determine if the number is divisible by two, by three, and by five
# respectively.
# Pass all the results to a final function that displays output on the screen - identifying whether or not the number
# is divisible by two, three, and five.


def main():
    number = int(input("Enter a number between 20 and 100: "))
    number = validate(number)
    print(divisible_by_two(number))
    print(divisible_by_three(number))
    print(divisible_by_five(number))


def validate(number):
    while number < 20 or number > 100:
        print("This is not valid value. ")
        number = int(input("Enter a whole number between 20 and 100: "))

    return number


def divisible_by_two(number):
    if number % 2 == 0:
        return str(number) + " is divisible by two"
    else:
        return str(number) + " is not divisible by two"


def divisible_by_three(number):
    if number % 3 == 0:
        return str(number) + " is divisible by three"
    else:
        return str(number) + " is not divisible by three"


def divisible_by_five(number):
    if number % 5 == 0:
        return str(number) + " is divisible by five"
    else:
        return str(number) + " is not divisible by five"


main()