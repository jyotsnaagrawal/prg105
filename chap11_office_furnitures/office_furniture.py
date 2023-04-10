class OfficeFurniture(object):
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set__category(self, category):
        self.__category = category

    def set__material(self, material):
        self.__material = material

    def set__length(self, length):
        self.__length = length

    def set__width(self, width):
        self.__width = width

    def set__height(self, height):
        self.__height = height

    def set__price(self, price):
        self.__price = price

    def get__category(self):
        return self.__category

    def get__material(self):
        return self.__material

    def get__length(self):
        return self.__length

    def get__width(self):
        return self.__width

    def get__height(self):
        return self.__height

    def get__price(self):
        return self.__price

    def __str__(self):
        return f'Category: {self.__category}\nMaterial: {self.__material}\nLength: {self.__length}\n'\
               f'Width: {self.__width}\nHeight: {self.__height}\nPrice: {self.__price}\n'



