def main():
    total = 0.0
    count = 0

    try:
        my_file = open("rainfall-totals.txt", "r")
        data_into_list = my_file.readlines()
        my_file.close()

        for line in data_into_list:
            split_line = line.rstrip('\n').split()
            month = split_line[0]
            amount = split_line[1]
            amount_list = amount.split('.')
            if amount_list[0].isdigit() and amount_list[1].isdigit():
                total += float(amount)
                count += 1
            else:
                print(f'Bad numeric data found for entry: {month} {amount}')

    except IOError:
        print(f'Unable to access the file.')

    average = total / count
    print(f"\n{count} good values were found. ")
    print(f"The total was {total:,.2f}. ")
    print(f"The average was {average:,.1f}. ")


main()



