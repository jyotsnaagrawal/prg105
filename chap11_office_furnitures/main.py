from desk import Desk
from office_furniture import OfficeFurniture


def main():

    office_furniture = OfficeFurniture("Desk", "Wood", 20, 50, 33, 100)
    desk = Desk("Wood", 56, 48, 56, 300, "Right", 6)
    print(office_furniture)
    print(desk)


main()
