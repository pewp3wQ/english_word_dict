class Words:

    def __init__(self, eng, rus):
        self.__rus = rus
        self.__eng = eng

    def set_rus_word(self, rus):
        self.__rus = rus

    def set_eng_word(self, eng):
        self.__eng = eng

    def get_rus_word(self, rus):
        return self.__rus

    def get_eng_word(self, eng):
        return self.__eng

    def __str__(self):
        return f'{self.__eng} - {self.__rus}'
