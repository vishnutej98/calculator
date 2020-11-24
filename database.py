
def addition(num1, num2):
    num3 = round((num1 + num2), 3)
    return num3


def subtraction(num1, num2):
    if num2 > num1:
        num3 = round((num2 - num1), 3)
        return num3
    else:
        num3 = round((num1 - num2), 3)
        return num3


def multiplication(num1, num2):
    num3 = round((num1 * num2), 3)
    return num3


def division(num1, num2):
    num3 = round((num1 / num2), 3)
    return num3
