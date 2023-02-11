# Directions :  Create a program that will have the user enter the total sales amount for the day at a coffee shop.
# The program should ask the user for the total amount of sales and include the day in the request.
# At the end of data entry, tell the user the total sales for the week, and the average sales per day.
#  You must create a list of the days of the week for the user to step through.
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
total_sales = 0
for day in days_of_the_week:
    amount_of_sales = float(input(f"What were the total sales for {day}: "))
    total_sales += amount_of_sales

print(f"The total amount of sales for the week was : {total_sales}")
# Calculate the total sales
print(f"The average amount of sales per day was : {total_sales / 7}")


