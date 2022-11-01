num = list(map(int, input().split(",")))
print(min(num))
print(max(num))
num = sorted(num)
del num[0]
del num[-1]
total = 0
for i in range(len(num)):
    total = num[0+i] + total
print(total)