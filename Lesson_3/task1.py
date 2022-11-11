inputSign = input("Choose sign : (+, -, *, /, sqrt, ^) ")
firstNumber = int(input("Input first number: "))
secondNumber = int(input("Input second number: "))

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error"

def exponentiation(number1, number2):
    return number1 ** number2

def rooting(number1, number2):
    return number1 ** (1 / number2)

def result(sign, number1, number2):
    match sign:
        case "+":
            print(addition(number1, number2))
        case "-":
            print(subtraction(number1, number2))
        case "*":
            print(multiplication(number1, number2))
        case "/":
            print(division(number1, number2))
        case "^":
            print(exponentiation(number1, number2))
        case "sqrt":
            print(rooting(number1, number2))

result(inputSign, firstNumber, secondNumber)