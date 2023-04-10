class Employee:
    def __init__(self, employee_name, employee_number ):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set__employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set__employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get__employee_name(self):
        return self.__employee_name

    def get__employee_number(self):
        return self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_numbered, hourly_pay_rate ):
        Employee.__init__(self, employee_name, employee_number)

        self.__shift_numbered = shift_numbered
        self.__hourly_pay_rate = hourly_pay_rate

    def set__shift_numbered(self, shift_numbered):
        self.__shift_numbered = shift_numbered

    def set__hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get__shift_numbered(self):
        return self.__shift_numbered

    def get__hourly_pay_rate(self):
        return self.__hourly_pay_rate

"""
class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift(self):
        return self.__shift

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate"""
