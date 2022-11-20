def sorting1():
    print("type your string :")
    dirtString = input()
    string = sorted(dirtString)
    print(string)

def  countElements2():
    print("type your string :")
    string = input()
    shortString = sorted(set(string))
    for letter in shortString:
        print(letter, "=", string.count(letter), end=" ")

def vowels3():
    print("type your string :")
    string = input()
    result = ""
    for letter in string:
        if letter in "aeiouAEIOU":
            result += letter
    print(result)

def consonants4():
    print("type your string :")
    string = input()
    result = ""
    for i in string:
        if i not in "aeiouAEIOU":
            result += i
    print(result)

def reverseString5():
    print("type your string :")
    string = list(input().split(" "))
    string.reverse()
    print(string)

def wordByIndex6():
    print("type your string :")
    string = list(input().split(" "))
    index = int(input())
    print(string[index - 1])

def oneMorePrint7():
    print("type your string :")
    string = input()
    print(string)
    print(string)


def number(operation1):
   match operation1:
       case 1:
           sorting1()
       case 2:
           countElements2()
       case 3:
           vowels3()
       case 4:
            consonants4()
       case 5:
            reverseString5()
       case 6:
            wordByIndex6()
       case 7:
            oneMorePrint7()
       case 8:
            exit()
       case _:
           print("Error")
print("Choose operation :(1 - sort string, 2 - count elements in string, 3 - print vowels, 4 - print consonants, 5 - reverse string, 6 - print by index, 7 - print string two times, 8 - exit")

operation1 = int(input())
number(operation1)
