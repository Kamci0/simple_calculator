import re


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Engine:
    def __init__(self):
        # instance variables
        self.equation = None
        self.qtab = []
        self.numbers_before = []
        self.numbers_after = []
        self.symbol = []
        self.result = None
        self.symbol_found = False

    def get_input(self, data):
        self.equation = data.replace(" ", "")

        self.equation = re.sub('[a-zA-Z]', '', self.equation)
        self.equation = re.sub(r"[\[\]{}()=&^%$#@!]", '', self.equation)

        for x in self.equation:
            self.qtab.append(x)

        self.symbol = re.findall(r"[+\-*/]", self.equation)

        for item in self.qtab:
            if item in self.symbol:
                self.symbol_found = True
            elif not self.symbol_found:
                self.numbers_before.append(item)
            elif self.symbol_found:
                self.numbers_after.append(item)

    def calcutale_result(self):
        if len(self.symbol) > 1:
            print("equation is to complex, use a single math symbol!")
        else:

            number_before = int(''.join(self.numbers_before))
            number_after = int(''.join(self.numbers_after))
            if "+" in self.symbol:
                self.result = add(number_before, number_after)
            elif "-" in self.symbol:
                self.result = subtract(number_before, number_after)
            elif "/" in self.symbol:
                self.result = divide(number_before, number_after)
            elif "*" in self.symbol:
                self.result = multiply(number_before, number_after)

    def get_result(self):
        return self.result
