Purchase_price = float(input(" Enter the purchase Price: "))
Selling_price = float(input(" Enter the selling Price"))

if Selling_price > Purchase_price:
    print(" product is in Profit")
elif Selling_price == Purchase_price:
    print("No profit, No loss")
else:
    print("Product is in loss")
