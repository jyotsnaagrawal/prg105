from office_furniture import OfficeFurniture


class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)

        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set__location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set__number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get__location_of_drawers(self):
        return self.__location_of_drawers

    def get__number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        return super().__str__() + f'Location_of_drawers: {self.__location_of_drawers}\n' \
                                   f'Number of drawers: {self.__number_drawers}'


