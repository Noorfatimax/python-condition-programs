# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd and if it's a multiple of 5
if number % 2 == 0:
    if number % 5 == 0:
        print("Even and a multiple of 5")
    else:
        print("Even")
else:
    if number % 5 == 0:
        print("Odd and a multiple of 5")
    else:
        print("Odd")
