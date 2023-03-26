class PersonData:
    def __init__(self):
        self.phone = None
        self.address = None
        self.age = None
        self.name = None

    def __int__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    # def __get__(self, instance, owner):

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def print(self):
        print(f'{self.name}, age {self.age}')
        print(self.address)
        print(self.phone + '\n')


def my_information():
    my_personal_information = PersonData()
    my_personal_information.set_name("Meri")
    my_personal_information.set_age(47)
    my_personal_information.set_address("8900 Route 14")
    my_personal_information.set_phone("123-456-7890")
    my_personal_information.print()

    my_friend_information = PersonData()
    my_friend_information.set_name("Mickey Mouse ")
    my_friend_information.set_age(93)
    my_friend_information.set_address("Anaheim, CA")
    my_friend_information.set_phone("800-123-4567")
    my_friend_information.print()

    my_family_information = PersonData()
    my_family_information.set_name("Donald Duck ")
    my_family_information.set_age(86)
    my_family_information.set_address("Anaheim, CA")
    my_family_information.set_phone("800-333-3333")
    my_family_information.print()


my_information()
