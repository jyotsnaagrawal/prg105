def main():
    total = 0.0
    count = 0
    print("This program will total and average number in your data file. ")
    file_name = input("Enter the name of your data file: ")

    try:
        sales_file = open(file_name, "r")

        line = sales_file.readline()
        while line != "":
            try:
                value = float(line)
                print(f"{value:,.2f}")
                total += value
                count += 1
            except ValueError:
                print(f'Line {count + 1} with a value of {line} was invalid.')

            line = sales_file.readline()

        sales_file.close()

    except IOError:
        print(f'Unable to access the file: {file_name}.')

    average = total / count
    print(f"\nTotal:.........{total:,.2f}")
    print(f"Number of entries:.....{count}")
    print(f"Average:........{average:,.2f}")


main()
