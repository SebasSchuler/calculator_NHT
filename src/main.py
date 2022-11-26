from controller.calculator import Calculator
calculator = Calculator()

op=""
result=""
while op != "end":
    print('Introduce operator:')
    op = input()
    print('Introduce first integer:')
    num1 = input()
    print('Introduce second integer:')
    num2 = input()

    if op == "+":
        result = calculator.add(int(num1), int(num2))
        print("The result of the sum is: " + str(result))
    elif op == "-":
        result = calculator.subtract(int(num1), int(num2))
        print("The result of the subtraction is: " + str(result))
    elif op == "*":
        result = calculator.multiplication(int(num1), int(num2))
        print("The result of the multiplication is: " + str(result))
    elif op == "/":
        result = calculator.division(int(num1), int(num2))
        print("The result of the division is: "+ str(result))
    elif op == "end":
        print("Closing calculator...")