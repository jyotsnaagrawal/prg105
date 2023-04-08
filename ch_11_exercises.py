"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors


class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.__number_of_rooms = number_of_rooms
        self.__square_feet = square_feet
        self.__floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)

    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.__square_feet = square_feet

    def set_floors(self, floors):
        self.__floors = floors

    # 3) Add accessors for all of the data attributes
    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def get_square_feet(self):
        return self.__square_feet

    def get_floors(self):
        return self.__floors


# 4) Create the class SingleFamilyHome as a subclass of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes


class SingleFamilyHome(Dwelling):
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    def get_garage_type(self):
        return self.__garage_type

    def get_yard_size(self):
        return self.__yard_size

    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size


# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
# 7) In main, create an object from the Single_family_home class with the following information:
#    6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres


def main():
    information = SingleFamilyHome(6, 1200, 1, 'single_car_garage', .25)

    # 8) Display the data using the accessor methods
    print('Number_of_rooms:', information.get_number_of_rooms())
    print('Square_feet:', information.get_square_feet())
    print('Floors:', information.get_floors())
    print('Garage_type:', information.get_garage_type())
    print('Yard_size:', information.get_yard_size())


# 9) Call the main function


main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)


# 1) Type in the mammal class from program 11-9, lines 1 - 22


class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        print('Grrrr')
# 2) Create a Mouse class as a subclass of the mammal class following the Dog example


class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    def make_sound(self):
        print('Woof! Woof!')


# 3) Create a Sheep class as a subclass of the mammal class following the Cat Example


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    def make_sound(self):
        print('Meow')


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Sheep class that you created


def main2():
    mammal = Mammal('regular animal')
    dog = Dog()
    cat = Cat()
    print('Here are some animals and')
    print('the sounds they make')
    print('-----------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


main2()
