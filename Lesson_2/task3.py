number = int(input())
for i in range(number):
    for k in range(number):
        print(number - k, end=" ")
    number -= 1
    print()
    