from file1 import ProductionWorker

day = 1
night = 2
unassigned = 3
print("Please enter employee data")
employee_name = input("Name: ")
employee_number = input("ID Number: ")
shift_numbered = int(input("Shift (1=day, 2=night, 3=unassigned): "))
hourly_pay_rate = float(input("Hourly Pay Rate: "))

worker = ProductionWorker(employee_name, employee_number, shift_numbered, hourly_pay_rate)
print("\nEmployee:", worker.get__employee_number(), worker.get__employee_name())
if 1 == day:
    print("Shift : day" )
elif 2 == night:
    print("Shift : night")
print("Pay Rate:", worker.get__hourly_pay_rate(), "per hour")







