def Add():
    num1=int(input("enter the first value :"))
    num2=int(input("enter the second value :"))
    add=num1+num2
    print(add)
            

def Sub():
    num1=int(input("enter the first value :"))
    num2=int(input("enter the second value :"))
    sub=num1-num2
    print(sub)
            

def Mul():
    num1=int(input("enter the first value :"))
    num2=int(input("enter the second value :"))
    mul=num1*num2
    print(mul)

def Div():
    num1=int(input("enter the first value :"))
    num2=int(input("enter the second value :"))
    div=num1/num2
    print(div)


msg="""
    Select operation
    
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    """

while True:
    print(msg)
    ch=int(input("enter the choice (1/2/3/4): "))
    if ch==1:
        Add()
    elif ch==2:
        Sub()
    elif ch==3:
        Mul()
    elif ch==4:
        Div()
    else:
        print("This is an Invalid input")
        quit()