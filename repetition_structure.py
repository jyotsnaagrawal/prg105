# Write a program that projects yearly income,the amount saved towards retirement each year, and total retirement
# savings. Assume a 3 percent raise on the starting income each year, and a 6% yearly return on investment.
# You will need to ask the user their current age, at what age they want to retire, what their current income is,
# what percent of their income they save each year, and how much they currently have in savings.
# You will calculate how many years until retirement,and display the projected income, savings contribution,
# and total savings each year.
age = int(input("How old are you currently ? "))
retirement_age = int(input("At what age do you want to retire ? "))
income = float(input("What is your yearly income ? "))
saving_percent = int(input("What percentage of your income do you save ? "))
savings = float(input("How much money do you currently have in saving ? "))
print("This projection assumes a 3% raise each year and a 6% yearly return on investment ")

print("year\t\tIncome\t\t\tSaving_contribution\t\tTotal_saving")

for year in range(retirement_age - age):
    year += 1
    contribution = income * (saving_percent / 100)
    savings = savings * 1.06  # 6% rate of return
    savings += contribution  # money added in the year
    print(f' {year}\t\t\t{round(income): ,}\t\t\t\t{round(contribution): ,}\t\t\t{round(savings): ,}')
    income = income * 1.03  # increasing salary by 3%
