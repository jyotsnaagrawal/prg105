"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# Write while loop that will change the variable in num by subtracting 1,
# then print the variable. Keep looping until num = 0, ie. while num > 0:
num = 10
while num > 0:
    num -= 1
    print(num)
# write your code here, the variable needs to exist before you start the loop


# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for-in loop with a list of the days of the week,
# print each day of the week
# SEE PROGRAM 4-6 FOR AN EXAMPLE
days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
for days in days_of_the_week:
    print(days)

# TODO 4.3 using range() in a for loop
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
for numbers in range(1, 10+1):
    print(numbers)

# TODO 4.3 using range() with a step value
print("=" * 10, "Section 4.3 using range() with a step value", "=" * 10)
# use the range function to print the odd numbers from 5 to 15
for numbers in range(5, 15):
    if numbers %2!= 0:
        print(numbers)

# TODO 4.3 using the control variable in a for loop
print("=" * 10, "Section 4.3 using the control variable in a for loop", "=" * 10)
# NOTE: The terms "Control Variable" and "Target Variable" both refer to the for loop variable
# 1) Write a for loop using range(1,10) and a control variable called number
# 2) Inside the loop, print the result of number times 7
for number in range(1, 10):
    number = (number * 7)
    print(number)

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered

# You can only enter 5 numbers
MAX = 5
# Initialize an accumulator variable.
total = 0

print("This program calculate the sum of", end='')
print(f" {MAX} numbers you will enter.")

for counter in range(MAX):
    number = int(input("enter a number: "))
    total = total + number

print(f'The total is {total}')


# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount. Initialize it to zero.
# Initialize another variable to store a count of the numbers entered.
# Use a while loop to have the user enter test scores until
# a sentinel value of -1 is entered.
# After the loop, display the total, the count, and the average (total / count)
test_score = 0
count = 0
total = 0
print("Enter test score to average ,when you are done ,enter -1 to stop \n")

while test_score >= 0:
    test_score = float(input("Please enter the next test score "))
    if test_score >= 0:
        total += test_score
    count +=1
average = total/count
print(f"{average:.2f} is the average of the {count} test score you entered")

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# input until the user enters a valid number. Test with
# both valid and invalid data.
number = int(input("Enter a number between 1 and 10:\n "))
while number < 1 or number > 10:
    print("ERROR: Invalid Number.\n ")
    number=int(input("Enter number between 1 and 10: "))
