import pickle

# Global constants
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
pickled_file = "customer_data.pkl"


def main():
    print("Welcome to your email list manager!\n")
    try:
        file = open(pickled_file, 'rb')
        customer_file = pickle.load(file)
    except IOError:
        customer_file = {}

    choice = 0
    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            read(customer_file)
        elif choice == ADD:
            create(customer_file)
        elif choice == CHANGE:
            update(customer_file)
        elif choice == DELETE:
            delete(customer_file)

    save(customer_file)


def menu():
    print("Enter your selection:")
    print("1. Look up a customer's email address")
    print("2. Add a new customer")
    print("3. Change an existing customer's email address")
    print("4. Delete a customer")
    print("5. Quit")

    choice = 0
    while choice not in [LOOK_UP, ADD, CHANGE, DELETE, QUIT]:
        try:
            choice = int(input("?"))
        except IOError:
            print("Invalid choice. Please enter a number from 1 to 5.")
    return choice


def read(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name in customer_file:
        print(customer_file[customer_name], "\n")
    else:
        print("No data found. Try adding a new entry.\n")


def create(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name not in customer_file:
        customer_email = input(f"Enter an email address of {customer_name}: ")
        customer_file[customer_name] = customer_email
        print(f"{customer_name} has been added with email {customer_email}.\n")
    else:
        print("Customer name already exists.\n")


def update(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name in customer_file:
        print(f"Current email for", customer_file[customer_name]+"."+"Do you want to change it? (y/n): ")
        confirm = input()
        if confirm.lower() == 'y':
            customer_email = input("Enter the new email address: ")
            customer_file[customer_name] = customer_email
            print("Customer data updated.")
        else:
            print("No changes made.\n")
    else:
        print("No record found for", customer_name, "\n")


def delete(customer_file):
    customer_name = input("Enter the name: ")
    if customer_name in customer_file:
        print("Current email for", customer_file[customer_name], "is." )
        confirm = input("Are you sure you want to delete this record? (y/n): ")
        if confirm.lower() == 'y':
            del customer_file[customer_name]
            print("Customer has been removed.")
        else:
            print("No changes made.\n")
    else:
        print("No record found for", customer_name, "\n")


def save(customer_file):
    try:
        file = open(pickled_file, "wb")
        pickle.dump(customer_file, file)
        file.close()
    except IOError:
        print("Unable to save file.")


main()
