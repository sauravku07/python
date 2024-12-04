# set
a = {"Ironman", "Hulk", "Thor", "Captain America", "Shaktimaan"}
b = {"Superman", "Batman", "Wonder-Woman", "Thor"}
c = {"Hulk", "Thor","Shaktimaan"}
'''
print(a)
print(type(a))
for x in a:
    print(x)
a.add("Spiderman")
print(a)

a.pop()
print(a)

a.remove("Thor")
print(a)

a.discard("Hulk")
print(a)

b = a.copy()
print(b)    '''
'''
# isdisjoint
print(a.isdisjoint(b))

# issubset
print(c.issubset(a))

# issubset
print(a.issuperset(c))

# update
a.update(c)
print(a)

# clear
a.clear()
print(a)     '''

'''
# union
print(a.union(c))

# Difference
print(a.difference(c))

# Difference update
a.difference_update(c)
print(a)   '''

# intersection
# print(a.intersection(c))

# Symmertic Difference
# x = a.symmetric_difference(c)
# print(x)
'''
# q1
d= {12, 56, 34, 35, 67, 2}
print(max(d))
print(min(d))

# q2
print(set(a) & set(b) & set(c))

# Q3
print(a.difference(b))

# q4
a.discard("Thor")
print(a) '''

# q5
print(c.issubset(a))
