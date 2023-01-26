cardNumber = str(input())
def validity(cardNumber):
    if len(cardNumber) == 16:
        list = ""
        for lenthCardNumber in range(8):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        halfcard = 0
        for values in list:
            halfcard += int(values)
        fullcard = 0
        for values in range(8):
            fullcard = fullcard + int(cardNumber[-1 - 2 * values])
        if (int(halfcard) + fullcard) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

    if len(cardNumber) == 15:
        list = ""
        for lenthCardNumber in range(7):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        print(list)
        halfcard = 0
        for values in list:
            halfcard += int(values)
        print(halfcard)
        fullcard = 0
        for values in range(8):
            fullcard = fullcard + int(cardNumber[-1 - 2 * values])
        print(fullcard)
        if (int(halfcard) + fullcard) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

    if len(cardNumber) == 13:
        list = ""
        for lenthCardNumber in range(6):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        print(list)
        halfcard = 0
        for values in list:
            halfcard += int(values)
        print(halfcard)
        fullcard = 0
        for values in range(7):
            fullcard = fullcard + int(cardNumber[-1 - 2 * values])
        print(fullcard)
        if (int(halfcard) + fullcard) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

def identification(firstCardNumber, secondCardNumber):
    numbers = firstCardNumber + secondCardNumber
    mastercard = ("51", "52", "53", "54", "55")
    amex = ("34", "37")
    if numbers in mastercard:
        print("MasterCard")
    elif identification in amex:
        print("AmEx")
    elif identification[0] == 4:
         print("Visa")
    else:
        print("Invalid")

validity(cardNumber)

