a = int(input("Enter first side of the trianle: "))
b = int(input("Enter 2nd side of the trianle: "))
c = int(input("Enter 3rd side of the trianle: "))

if a==b and b==c:
    print("Triangle is equilateral")
elif a==b or b==c or c==a:
    print("Triangle is isosciles")
else:
    print("Triangle is scalene")