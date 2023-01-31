
# This program for monthly income and expenses
print("This Program will helps someone create a budget")

# input from user for ask their monthly income and expenses

monthly_income=float(input("How much is  your total monthly Income?"))
housing_expenses: float=float(input("How much do you spend on your housing each month?"))
food_expenses=float(input("How much do you spend on your food each month?"))
transportation_expenses=float(input("how much do you spend on your transportation on each month?"))
phone_bill_expenses=float(input("how much do you spend on your phone bills each month?"))
utilities_expenses=float(input("how much do you spend on your utilities bills each month?"))
clothing_expenses=float(input("how much do you spend on your clothing each month?"))

#  calculate and display the income percentage of each budget item.
housing_expenses_per = (housing_expenses / monthly_income)
food_expenses_per = (food_expenses / monthly_income)
transportation_expenses_per = (transportation_expenses / monthly_income)
phone_bill_expenses_per = (phone_bill_expenses / monthly_income)
utilities_expenses_per = (utilities_expenses / monthly_income)
clothing_expenses_per = (clothing_expenses / monthly_income)
# display results
print(f"\nHousing expenses takes up {housing_expenses_per:.2%} of your monthly income.")
print(f"Food expenses takes up {food_expenses_per:.2%} of your monthly income.")
print(f"Transportation takes up {transportation_expenses_per:.2%} of your monthly income.")
print(f"Phone bills takes up {phone_bill_expenses_per:.2%} of your monthly income.")
print(f"Utilities takes up {utilities_expenses_per:.2%} of your monthly income.")
print(f"Clothing takes up {clothing_expenses_per:.2%} of your monthly income.\n")

total_expenses = housing_expenses + food_expenses + transportation_expenses + phone_bill_expenses + utilities_expenses \
                 + clothing_expenses
savings = monthly_income - total_expenses
print(f"You have ${savings} left from your income after paying these monthly expenses.")