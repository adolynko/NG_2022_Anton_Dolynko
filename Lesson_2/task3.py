number = int(input())
for row in range(number):
    for pillar in range(number):
        print(number - pillar, end=" ")
    number -= 1
    print()
    