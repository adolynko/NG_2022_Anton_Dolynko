string = input()
shortString = sorted(set(string))
for k in shortString:
    print(k,"=", string.count(k))