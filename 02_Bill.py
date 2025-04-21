from enum import global_str

name = input("Enter your name: ")
cost = float(input(" Enter the cost: "))
quantity = float(input("Enter the quantity: "))
amount= cost * quantity
gst = 2 * amount / 100
total = amount + gst
if total < 1000:
    discount=0
elif total <3000:
    discount= 0.1 * total
    print("Congratulations, You,ve availed discount of 10% for your purchase")
else:
    discount= 0.2 * total
    print("Congratulations, You,ve availed discount of 20% for your purchase")

print("----------")
print("Billed Amount: " ,amount)
print("gst: ",gst)
print("Discount: " ,discount)
print("Amount to be paid: ",total - discount)
print("----------")



