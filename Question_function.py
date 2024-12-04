# Ques_1
def maximum_num(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        print(val1, " is the greatest number")
    elif val2 > val1 and val2 > val3:
        print(val2, " is the greatest number")
    else:
        print(val3, " is the greatest number")
maximum_num(12, 5, 8)


# Question 2
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)

    return l
print(create_list())

# Question 3
def check_prime(num):
    if num == 1:
        print("it is not a prime number")
    if num == 2:
        print("it is a prime number")
    if num > 2:
        for i in range (2 , num):
             if num % i == 0:
                print("it is not a prime number")
                break
        else:
            print("it is a prime number")
check_prime(110)

# Question 4
def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return (total)
print(add([12,4,5,6,7,8]))

# Question 5
def fibonanci(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fibonanci(num-1) + fibonanci(num-2))
print(fibonanci(7))




