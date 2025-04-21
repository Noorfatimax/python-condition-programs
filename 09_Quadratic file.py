a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b * b - 4 * c

if d < 0:
    print("No real roots")
elif d == 0:
    r1 = r2 = -b/(2*a)
    print("Real roots" ,r1 , r2)

else:
    r1 = (-b + d ** 0.5 / (2 * a))
    r2 = (-b - d ** 0.5 / (2 * a))
    print("Real & Unequal roots are" ,r1 ,r2)


