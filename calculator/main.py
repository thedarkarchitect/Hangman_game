from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def Calculator():
    #Here the functionn in dictionary is saved in variable to be used as a function
    print(logo)
    operations = {"+": add, 
                "-": subtract, 
                "*": multiply, 
                "/":divide
                }

    num1 = float(input("What's the first number? "))


    for key in operations:

        print(key)

    still_on = True

    while still_on:
        
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number?: "))
        cal_function = operations[operation_symbol]
        answer = cal_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with 8, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            still_on = False
            #using recussion to start a new calculation but to avoid it being infinite you must have a condition to control the while loop
            Calculator()


Calculator()



