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

