name = input(" Enter your name: ")
english = float(input(" Enter your marks in english: "))
maths = float(input(" Enter your marks in maths: "))
science = float(input(" Enter your marks in science: "))
physics = float(input(" Enter your marks in physics: "))
chemistry = float(input(" Enter your marks in chemistry: "))
total = english + science + maths + physics + chemistry
percentage = total/5
print("--------------")
print(" Report card for" ,name)
print("---------------------")
print("Total marks scored", total)
print("Percentage", percentage, "%")
if percentage >=40:
      print("   Congratulations!!!")
else:
      print("Sorry! Better Luck next time")
print("---------------------")