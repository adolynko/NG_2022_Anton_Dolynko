number = list(map(int, input().split(",")))
print(min(number))
print(max(number))
num = sorted(number)
del number[0]
del number[-1]
total = 0
for element in range(len(number)):
    total = number[0+element] + total
print(total)