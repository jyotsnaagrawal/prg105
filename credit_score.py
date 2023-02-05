# For this assignment, you will be providing the logic (plan) for the following program:
# Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit.
# Credit score range:-
# Bad = 300 - 629
# Fair = 630 – 689
# Good = 690 – 719
# Excellent =720 - 850

# get credit score from user.

credit_score =int(input(" What is your credit score?"))
print(f" With a credit score of {credit_score}")

# Do they have Bad, Fair, Good, or Excellent credit :

if (credit_score >= 300) and (credit_score <= 629):
    credit = "bad"
elif (credit_score >= 630) and (credit_score <= 689):
    credit = "fair"
elif (credit_score >= 690) and (credit_score <= 719):
    credit = "good"
elif (credit_score >= 720) and (credit_score <= 850):
    credit = "excellent"
else:
    credit = "invalid"

print(f" you have {credit} credit score.")


