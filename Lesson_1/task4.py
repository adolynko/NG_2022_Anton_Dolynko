a = int(input())
b = int(input())
c = int(input())
#ax^2+bx+c=0
d=b**2-4*a*c
if d<0:
  print("there are no solutions")
elif d == 0:
  print(-b / (2*a))
elif d > 0:
  x1 = (-b - d ** 0.5) / (2*a)
  x2 = (-b + d ** 0.5) / (2*a)
  print(x1)
  print(x2)