def exponent(x, y):
    return x ** y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Division by zero!"
    else:
        return x / y

def addition(x,y):
    return x + y

def subtraction(x, y):
    return x - y 

while True:
    print("""
    1.Exponent
    2. Multiplication
    3. Division
    4. Addition
    5. Subtraction
    """)
    user_operation = int(input("Input the operation that you would like to perform: "))
    if user_operation == 1:
        base_number = int(input("What is the base number you would like to use: "))
        multi = int(input("What would you like to multiply: "))
        print(f"The result is: {exponent(base_number, multi)}")
    elif user_operation == 2:
        first_num = int(input("What is the first number that you would like to use: "))
        multi = int(input("What would you like to multiply: "))
        print(f"The result is: {multiplication(first_num, multi)}")
    elif user_operation == 3:
        first_num = int(input("What is the first number that you would like to use: "))
        div = int(input("What is the number that you would like to divide: "))
        print(f"The result is: {division(first_num, div)}")
    elif user_operation == 4:
        first_num = int(input("What is the first number that you would like to use: "))
        second_num = int(input("What is the second number that you would like to use: "))
        print(f"The result is: {addition(first_num, second_num)}")
    elif user_operation == 5:
        first_num = int(input("What is the first number that you would like to use: "))
        second_num = int(input("What is the second number that you would like to use: "))
        print(f"The result is: {subtraction(first_num, second_num)}")
    else:
        print("You have chosen a nonexistant choice pick another operation")