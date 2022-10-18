print("choose a sign:'+','-','*','/','sqrt','squaring'. ")
sign = str(input())
if sign == "sqrt":
  print('Enter number: ')
  num4 = int(input())
  print(num4**(1/2))
  exit()
if sign == "squaring":
  print('Enter number: ')
  num3 = int(input())
  print(num3**2)
  exit()
print('Enter two numbers: ')
num1 = int(input())
num2 = int(input())
if sign == "-":
  print(num1-num2)
elif sign == "+":
  print(num1+num2)
elif sign == "*":
  print(num1*num2)
elif sign == "/" and num2 > 0:
  print(num1/num2)
else:
  print("Error")
