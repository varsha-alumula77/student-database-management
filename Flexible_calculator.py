from functools import reduce


def addition(*numbers):
    add = reduce(lambda x, y: x + y , numbers)
    return add

def multiply(*numbers):
    mul = reduce(lambda x, y: x * y , numbers)
    return mul

def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number - 1)


operator = input("Enter the operation: ")

if operator in ('+', 'addition', 'add'):
    numbers = tuple(
        map(int, input("Enter the number separated by space: ").split())
        )
    print(addition(*numbers)) 

elif operator in ('*', 'multiplication', 'mul' ):
    numbers = tuple(
        map(int, input("Enter the numbers separated by space: ").split())
        )
    print(multiply(*numbers))

elif operator in ('!', 'factorial' ,'fact'):
    number = int(input("Enter the number: "))
    print(factorial(number))

else:
    print("Please choose valid operation from (+,*,!)")

