units = int(input(" Enter the no. of units consumed: "))
if units < 200:
    bill = 200 * 4
elif units < 500:
    bill = 800 + (units - 200) * 6
elif units < 800:
    bill = 800 + 1800 + (units - 500) * 8
else:
    bill = 800 + 1800 + 2400 + (units - 800) * 10

print(" Total Bill" ,bill)