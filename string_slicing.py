greeting = "Good Morning, "
name = "devil"
print(greeting + name)
c = greeting + name 
# concatenating two strings
print(c)
print(name[3])
# name[3] = "d"           #--> Does not work
print(name[0:3])
print(name[0:])           # is same as name[0:4]
print(name[2:])           # is same as name[2:4]
c = name[-4:-2]           # is same as name[1:3]
print(c)
name = "devilpsgocd"
d = name[1:9:3]
print(d)