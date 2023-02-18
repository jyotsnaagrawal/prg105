# Create a program that presents the user with five choices. The topic could be game characters, food, car packages, or
# anything you are interested in. You will put a menu on the screen,ask the user to enter the number or letter of their
# choice, and then call the corresponding function to give the user more information

def menu():
    print("Select one of the menu options below to find out more ")
    print("[1] Paneer Tikka ")
    print("[2] Nintendo ")
    print("[3] Butter Naan ")
    print("[4] Elsa and Anna ")
    print("[5] Chhole ")


menu()
number = int(input("Please enter the number of your choice: "))


def paneer_tikka():
    print("Fresh Paneer spicy cubes with a side of two butter naan. ")


def nintendo():
    print("Nintendo Entertainment System (NES), was released as the Famicom in Japan on July 15, 1983. ")


def butter_naan():
    print("Butter naan with a side of vegetable. ")


def elsa_and_anna():
    print("Anna is depicted as the princess of Arendelle, a fictional Scandinavian kingdom,")
    print("and the younger sister of Elsa (Idina Menzel),who is the heiress to the throne and ")
    print("possesses the elemental ability to create and control ice and snow.. ")


def chhole():
    print("Indian style chhole curry made with white chickpeas.")


if number == 1:
    paneer_tikka()
elif number == 2:
    nintendo()
elif number == 3:
    butter_naan()
elif number == 4:
    elsa_and_anna()
elif number == 5:
    chhole()

else:
    print("Invalid number. ")






