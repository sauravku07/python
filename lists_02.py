# Create a list using []
a = [2, 4, 6, 7, 8]
print(a[0])
# Change the value of list using
a[2] = 45
print(a)
# we can create a list with items of different types
c = [45, "Harry ", False, 6.9]
print(c)
# List slicing 
friends = ["devil", "Thakur", "Boss", "Raunak", "Nilesh"]
print(friends[0:3])

# for loop
for i in friends:
    print(i)

for i in range(len(friends)):
    print(friends[i])
# while loop
i = 0
while i < len(friends):
    print(friends[i])
    i += 1

# short-Hand for loop
[print(i) for i in friends]
