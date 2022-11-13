string = input()
shortString = list(set(string))
def countLetters(text):
    if len(shortString) > 0:
        print(shortString[0],'=',string.count(shortString[0]),', ',end='')
        shortString.remove(shortString[0])
        countLetters(text)
countLetters(shortString)
