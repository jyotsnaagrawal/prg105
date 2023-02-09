# Sentinel values, Accumulators, and Data Validation are tools you will use often

print('*********** Ending a loop by entering a SENTINEL VALUE ***********')
print('Showing multiples of 5')
# *************************************************************************************************************
# A Sentinel value is a special value used to trigger the end of a loop
# Sentinel values are often used when getting multiple input values from the keyboard
# our special or

# When getting data from the user, clue them in about the sentinel value you are looking for
# the sentinel value must be a value that will not be valid data for the situation

# sentinel value for this loop is 0
in_value = int(input("\nEnter a number (0 to quit) :"))
while in_value != 0:
    print(f"{in_value} times 5 is {in_value * 5}")
    in_value = int(input("\nEnter a number (0 to quit) :"))
# don't forget to get the next value

print('\n*********** Using ACCUMULATOR variable(s) in a loop ***********')
print('Averaging test scores')
# *************************************************************************************************************
# An Accumulator is a variable used to add up values in a loop
# before you use the accumulator, make sure it is set to the correct initial value, usually zero

# initialize accumulator
total = 0
# if calculating an average, I also need to count the values, so I need a second accumulator
count = 0
# since 0 is a valid test score, this loop uses -1 as the sentinel value
in_value = int(input("\nEnter test score (-1 to quit):"))
while in_value != -1:
    # add this score to the total and add one to the count of scores
    total += in_value
    count += 1
    in_value = int(input("\nEnter test score (-1 to quit):"))

  # get the next value


# calculate the average once all values have been entered (outside the loop)
# NOTE: if no values were entered, the count is zero and division by zero will generate an error
if count > 0:
    average = total / count
    print(f"{count}scores,the average is {average}")
else:
    print("No data.")
# if the number of needed iterations are known, a for loop could be used
num_scores = 5
print(f'\nAverage for {num_scores} test scores')

# since the number of tests is known in this scenario, we do not need an accumulator for the count
total = 0
for score in range(1, num_scores +1):
    in_value = int(input(f"\nEnter score for test {score}: "))
    total += in_value
    print(f"\nFor {num_scores} scores, the average is {total /num_scores}")


print('*********** Using a while loop to validate data ***********')
# *************************************************************************************************************
# A Data Validation loop tests for a valid input value and, IF INVALID,
#     repeatedly requests a new value until a valid value is entered.

# prompt the user to enter a valid choice
choice = input("\nChoose an option (A, B , C ): ")
choice = choice.upper()   # .upper() function converts lower to upper in string.
# for this example, assume the user needs to enter an uppercase response
# the while loop should test for BAD data so that good data will cause the loop to exit
# if the initial value entered is a good value, the loop will never fire
while choice != "A" and choice != "B" and choice != "C":
    # since bad data was found, give an error and prompt again
    choice = input("\nSorry you need to be enter A, B ,or  C : ")
    choice = choice.upper()

# the data validation loop only exits once good data has been received
print(f"You selected {choice}")
