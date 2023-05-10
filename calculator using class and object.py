class Calculator:
    #craeted a class calculator
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        #method to perform addition
        add = num1 + num2
        return add

    def sub(self, num1, num2):
        # method to perform subtraction
        sub = num1 - num2
        return sub

    def mul(self, num1, num2):
        # method to perform multiplication
        mul = num1 * num2
        return mul

    def div(self, num1, num2):
        try:
            div = num1 / num2
            return div
        # Exception handling in case of division by zero or other errors
        except Exception as solve:
            return solve

    def power(self, num1, num2):
        # Method to calculate the power of a number
        return pow(num1, num2)

#menu message
msg = """
    Select operation

    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power
    6. Quit
"""

#main function
def main():
    while True:
        print(msg)
        #user input choice
        ch = int(input("Enter the choice (1/2/3/4/5/6): "))

        firstvalue = int(input("Enter the first value: "))
        secondvalue = int(input("Enter the second value: "))

        operation = Calculator(firstvalue, secondvalue)

        if ch == 1:
            print(operation.add(firstvalue, secondvalue))

        elif ch == 2:
            print(operation.sub(firstvalue, secondvalue))

        elif ch == 3:
            print(operation.mul(firstvalue, secondvalue))

        elif ch == 4:
            print(operation.div(firstvalue, secondvalue))

        elif ch == 5:
            print(operation.power(firstvalue, secondvalue))

        elif ch == 6:
            break

        else:
            print("This is an invalid choice. Please try again.")

#calling main function
if __name__ == "__main__":
    main()
