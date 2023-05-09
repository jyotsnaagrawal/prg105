class Questions:
    def __init__(self, q, a1, a2, a3, a4, correct):
        self.__question = q
        self.__answer1 = a1
        self.__answer2 = a2
        self.__answer3 = a3
        self.__answer4 = a4
        self.__correct_answer = correct

    def set_question(self, q):
        self.__question = q

    def set_answer1(self, a1):
        self.__answer1 = a1

    def set_answer2(self, a2):
        self.__answer2 = a2

    def set_answer3(self, a3):
        self.__answer3 = a3

    def set_answer4(self, a4):
        self.__answer4 = a4

    def set_correct(self, correct):
        self.__correct_answer = correct

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct_answer(self):
        return self.__correct_answer

    def __str__(self):
        return "\n" + self.__question + "\n" + self.__answer1 + "\n" + self.__answer2 + "\n" + self.__answer3 + "\n" +\
            self.__answer4 + "\n" + self.__correct_answer
