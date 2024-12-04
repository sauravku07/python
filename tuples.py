a = "2", "3", "6", "9", "10"
print(type(a))
print(a)
b = "ironman",
print(type(b))


# slicing
'''
print(a[1:3])
print(a[:3])
print(a[::2])    '''

# with for loop
'''
for i in a:
    print(i)   '''

# along wth range and length in for loop
'''
for i in range(len(a)):
  print(a[i])    '''

# along with while loop
'''
i=0
while i < len(a):
    print(a[i])
    i += 1     '''

# conversion in tuple
'''
print("before conversion", type(a))
print(a)
a = list(a)
print("after conversion ", type(a))
a.append("5")
print(a)     '''
