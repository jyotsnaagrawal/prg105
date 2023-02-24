def main():
    num_people = int(input("How many people do you want to add to the file? "))
    contact_information_file = open("information.txt", "w")
    # add people to the file
    while num_people > 0:
        name = input("What is the name of the person? ")
        phone_number = input("What is their phone number? ")
        email_address = input("What is their email address? ")

        contact_information_file.write(f"{name}, {phone_number}, {email_address}\n")
        num_people -= 1
    contact_information_file.close()


main()









