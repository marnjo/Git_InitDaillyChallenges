def calculator():
    con = "Y"
    while con.upper() != "N":
        firstNumber = int(input("Enter the first number: "))
        operator = input("Enter the operator you wish to use: ")
        secondNumber = int(input("Enter the second number: "))

        if operator == "+":
            result = firstNumber + secondNumber
            print(result)
        elif operator == "-":
            result = firstNumber - secondNumber
            print(result)
        elif operator == "*":
            result = firstNumber * secondNumber
            print(result)
        elif operator == "/":
            result = firstNumber / secondNumber
            print(result)
        else:
            print("Invalid input")
            calculator()
        con = input("Do you wish to continue (Y/N)")

calculator()
