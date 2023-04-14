import re

equation = ""

while equation != "0":
    equation = input("Enter you equation here, 0 to close: ").replace(" ", "")
    equation = re.sub('[a-zA-Z]', '', equation)
    equation = re.sub(r"[\[\]{}()=]", '', equation)
    qtab = []
    numbers_before = []
    numbers_after = []
    symbol = []
    symbol_found = False
    result = 0

    for x in equation:
        qtab.append(x)

    symbol = re.findall(r"[+\-*/]", equation)

    if len(symbol) > 1:
        print("equation is to long ")
        break
    else:
        for item in qtab:
            if item in symbol:
                symbol_found = True
            elif not symbol_found:
                numbers_before.append(item)
            elif symbol_found:
                numbers_after.append(item)

        number_before = int(''.join(numbers_before))
        number_after = int(''.join(numbers_after))
        if "+" in symbol:
            result = number_before + number_after
        elif "-" in symbol:
            result = number_before - number_after
        elif "/" in symbol:
            result = number_before / number_after
        elif "*" in symbol:
            result = number_before * number_after

        print(f"The result of the equation : {number_before} {str(''.join(symbol))} {number_after} is {result}")
