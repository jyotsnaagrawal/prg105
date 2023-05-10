class Person:

    def __init__(self, name, age, address, phone):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

    # def __get__(self, instance, owner):

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def print(self):
        print(f'{self.name}, age {self.age}')
        print(self.address)
        print(self.phone + '\n')

    def __str__(self):
        return "Name: " + self.__name + "\nAddress " + self.__address + "\nAge " + self.__age + "\nPhone "\
            + self.__phone


def main():
    person1 = Person("Ram", "567 Treeline Dr, Crystal Lke", "35", "224-567-789\n")
    person2 = Person("Poonam", "768 Treeline Dr, Crystal Lke", "35", "224-567-789\n")
    person3 = Person("Geeta", "234 Treeline Dr, Crystal Lke", "35", "224-567-789")
    print(person1)
    print(person2)
    print(person3)


main()
