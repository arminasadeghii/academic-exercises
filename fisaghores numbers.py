a = int(input())
b = int(input())
c = int(input())

if a**2 + b**2 == c**2:
    print("YES")
elif a**2 == b**2 + c**2:
    print("YES")
elif a**2 + c**2 == b**2 : 
    print("YES")
else:
    print("NO")