# for loop
'''
for i in range(1, 11):
    print(7, "*", i, "=", 7*i)   '''

# while loop
'''
n = 0
while n <= 5:
    print(n)
    n += 1    '''

# while true
'''
n = 0
while True:
    print(n)
    n += 1     '''

# Nested Loops
'''
for i in range(1, 4):
    for j in range(1, 11):
        print(j, end=" ")
    print()        '''

# For loop with Conditional Statements
'''
for i in range(1, 11):
    if i == 3:
        print("my favs number")
    else:
        print(i)     '''

# Break and continue statements
'''
for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)

for i in range(1, 11):
    if i == 5:
        break
    else:
        print(i)          '''


# Question 1
'''
sum = 0
for i in range(0,51):
    if i % 2 == 0:
        sum += i
print("sum of  even number up to 50 is ", sum)    '''

# Question 2
'''
for i in range(1,21):
    print(i,"sqaure is ", i**2)     '''

# Question 3
'''
sum = 0
n=0
while n <= 20:
    if n%2 != 0:
        sum += n
    n += 1
print("sum of 10 odd number is", sum )   '''

# Question 4
'''
for i in range(1,101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)   '''

# Question 5
while True:
    name = input("enter customer's name: ")
    total = 0

    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes?no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name: ", name)
    print("Amount to be paid: ",total)
    print("_"*40)
    print("********Happy Shopping*********")

    repeat1 = input("do you want to go to next customer? (yes?no): ")
    if repeat1 == "no" or repeat1 == "No":
        break