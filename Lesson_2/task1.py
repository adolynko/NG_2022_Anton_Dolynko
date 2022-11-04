string = input()
shortString = sorted(set(string))
for letter in shortString:
    print(letter,"=", string.count(letter))