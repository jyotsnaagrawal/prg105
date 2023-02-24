# Direction : - Write a program that will read numeric data from a text file line by line using a loop.
# Strip the newline and convert each value to a float, then display it. Use variables to count and total the entries.
# At the end, display the total, count and average of the values.

def main():
    count = 0
    total = 0.0
    sales_file = open("sales_totals.txt", "r")

    line = sales_file.readline()
    while line != "":
        value =float(line)
        print(f"{value:,.2f}")
        total += value
        count += 1
        line = sales_file.readline()

    sales_file.close()
    average = total/count
    print(f"\n\nTotal..........{total}")
    print(f"Number of entries........{count}")
    print(f"Average:...........{average}")


main()


