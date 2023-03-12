def main():
    try:
        accounts_file = open("accounts.txt", "r")
        accounts_list = [line.strip().split(',') for line in accounts_file.readlines()]
        overdue_file = open("over90.txt", "r")
        overdue_list = [line.strip() for line in overdue_file.readlines()]
        accounts_file.close()
        overdue_file.close()

    except FileNotFoundError:
        print("Error: One or both files not found")
        exit()
    overdue_accounts_list = []
    for account in accounts_list:
        if account[0] in overdue_list:
            overdue_accounts_list.append(account)

    for account in overdue_accounts_list:
        print(", ".join(account[0:7]))


main()