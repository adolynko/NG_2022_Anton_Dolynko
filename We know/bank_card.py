cardNumber = str(input())
def validity(cardNumber):
    if len(cardNumber) == 16:
        list = ""
        for lenthCardNumber in range(8):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        list1 = 0
        for everyValueInList in list:
            list1 += int(everyValueInList)
        list2 = 0
        for i in range(8):
            list2 = list2 + int(cardNumber[-1 - 2 * i])
        if (int(list1) + list2) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

    if len(cardNumber) == 15:
        list = ""
        for lenthCardNumber in range(7):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        print(list)
        list1 = 0
        for everyValueInList in list:
            list1 += int(everyValueInList)
        print(list1)
        list2 = 0
        for i in range(8):
            list2 = list2 + int(cardNumber[-1 - 2 * i])
        print(list2)
        if (int(list1) + list2) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

    if len(cardNumber) == 13:
        list = ""
        for lenthCardNumber in range(6):
            list = list + str(int(cardNumber[-2 - 2 * lenthCardNumber]) * 2)
        print(list)
        list1 = 0
        for everyValueInList in list:
            list1 += int(everyValueInList)
        print(list1)
        list2 = 0
        for i in range(7):
            list2 = list2 + int(cardNumber[-1 - 2 * i])
        print(list2)
        if (int(list1) + list2) % 10 == 0:
            identification(cardNumber[0], cardNumber[1])
        else:
            print('Invalid')

def identification(firstCardNumber, secondCardNumber):
    a = firstCardNumber + secondCardNumber
    mastercard = ("51", "52", "53", "54", "55")
    amex = ("34", "37")
    if a in mastercard:
        print("MasterCard")
    elif identification in amex:
        print("AmEx")
    elif identification[0] == 4:
         print("Visa")
    else:
        print("Invalid")

validity(cardNumber)

