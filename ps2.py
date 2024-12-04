# Write a program to check if a number is positive
"""num = int(input("enter a number here: "))
if num > 0:
    print("it is positive")   """

# Write a program to check whether a number is odd or even.
'''num = int(input("enter a number here: "))
if num % 2 == 0:
   print("it is even number")
else:
    print("it is odd number")  '''

# write a program to create area calculator
'''
print("****AREA CALCULATOR****")
print(""" press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle """)

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    side = float(input("enter the length of a side: "))
    area = side**2
    print("the area of square is ",area)

elif choice == 2:
    length =float(input("enter the length of a rectangle: "))
    width = float(input("enter the width of a rectangle: "))
    area = length*width
    print("the area of rectangle is ",area)

elif choice == 3:
    radius = float(input("enter the radius of a circle: "))
    area = 3.24*(radius**2)
    print("the area of circle is ",area)

elif choice == 4:
    base = float(input("enter the base of a triangle: "))
    height = float(input("enter the height of a triangle: "))
    area = 0.5*base*height
    print("the area of triangle is ", area)

else:
    print("invalid input") '''

# Write a program check whether the passed letter is vowel or not
'''
letter = input("enter a letter here: ")
if letter in "aeiou or AEIOU":
    print("it is a vowel")
else:
    print("it is not a vowel")   '''

# write a program to check if a number is a single digit number,2-digit number upto 5 digit
num = int(input("enter a number here up to 5 digit: "))
if num >= 0 and num <= 9:
    print("it is 1 digit number")
elif num >= 10 and num <= 99:
    print("it is 2 digit number")
elif num >= 100 and num <= 999:
    print("it is 3 digit number")
elif num >= 1000 and num <= 9999:
    print("it is 4 digit number")
elif num >= 10000 and num <= 99999:
    print("it is 5 digit number")