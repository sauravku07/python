'''
def hello():
    print("Hello world")

hello()
def add(x, y):
    print(x+y)

add(13,87)

# Return function
def add(a,b):
    return (a+b)
print(add(12,4))

# Recursion function

def hello():
    print("hello")
    return hello()
print(hello())    '''

#factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))
print(fact(5))