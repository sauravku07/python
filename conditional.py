# if statement
marks = 97
if marks >= 90:
    print("you won a gift")
print("Thank you")

# if-else statement
marks = 82
if marks >= 85:
    print("you won gift")
else:
    print("you need more study")

# if-elif-else statement
marks = 98
if marks >= 95:
    print("A+")
elif marks < 95 and marks >= 85:
    print("A")
else:
    print("B")

# Nested if statement
marks = 97
if marks >= 85:
    print("you got new phone")
    if marks >= 95:
        print("you can go to a trip")
else:
    print("no phone for a month")

#short hand if statement
marks = 97
if marks >= 90: print("you will get a new phone")

#Short hand if-else statement
marks = 87
print("you will go to a trip") if marks >= 90 else print("no phone for a month")
