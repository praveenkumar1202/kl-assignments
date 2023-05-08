import math 
class Area:  
    def Area_Square(self):
        area=int(input("enter the area of the square: "))
        return pow(area,2)
    def Area_Rectangle(self):
        length=int(input("enter the length of the rectangle :"))
        breadth=int(input("enter the breadth of the rectangle:"))
        return (length+breadth)
    def Area_Triangle(self):
        base=(int(input("enter the base of the triangle:")))
        height=(int(input("enter the height of the triangle :")))
        return (0.5*base*height)
    def Area_circle(self):
        area=int(input("enter the area of the circle:"))
        return math.pi*area*area
    def Area_parallelogram(self):
        breadth=int(input("enter the breadth of the parallelogram :"))
        height=(int(input("enter the height of the parallelogram :")))
        return breadth*height
    
    
class perimeter:
    def Perimeter_Square(self):
        area=int(input("enter the area of the square: "))
        return 4*area
    def Perimeter_Rectangle(self):
        length=int(input("enter the length of the rectangle :"))
        breadth=int(input("enter the breadth of the rectangle:"))
        return 2*(length+breadth)
    def Perimeter_Triangle(self):
        side=int(input("enter the side of the triangle :"))
        return (side+side+side)
    def Perimeter_circle(self):
        radius=int(input("Enter the radius of the circle :"))
        return 2*math.pi*radius
    def Perimeter_parallelogram(self):
        area=int(input("enter the area of the parallelogram  :"))
        breadth=int(input("enter the breadth of the parallelogram :"))
        return(2*(area+breadth))
    
display="""
        Select any one  of the following options
        1. Square
        2. Rectangle
        3. Triangle
        4. Circle
        5. Parallelogram
"""
AreaPerimeter ="""
        Select any one  of the following options
        1.Area
        2.Perimeter
"""

objectArea=Area()
objectPerimeter=perimeter()
while True:
    print(display)
    choice=int(input("Enter a choice (1/2/3/4/5): "))
    if choice==1:
        print(AreaPerimeter)
        message = int(input("Enter a choice (1/2):"))
        if message == 1 :
            print(objectArea.Area_Square()) 
        elif message == 2:
            result=objectPerimeter.Perimeter_Square()
            print(result)
        else:
            print("invalid option")
    elif choice==2:
        print(AreaPerimeter)
        message = int(input("Enter a choice (1/2):"))
        if message==1:
            print(objectArea.Area_Rectangle())
        elif message==2:
            print(objectPerimeter.Perimeter_Rectangle())  
        else:
            print("invalid option")
    elif choice==3:
        print(AreaPerimeter)
        message = int(input("Enter a choice (1/2):"))
        if message==1:
            print(objectArea.Area_Triangle())
        elif message==2:
            print(objectPerimeter.Perimeter_Triangle())
        else:
            print("invalid option")
    elif choice==4:
        print(AreaPerimeter)
        message = int(input("Enter a choice (1/2):"))
        if message==1:
            print(objectArea.Area_circle())
        elif message==2:
            print(objectPerimeter.Perimeter_circle())
        else:
            print("invalid option")
    elif choice==5:
        print(AreaPerimeter)
        message = int(input("Enter a choice (1/2):"))
        if message==1:
            print(objectArea.Area_parallelogram())
        elif message==2:
            print(objectPerimeter.Perimeter_parallelogram())
        else:
            print("invalid option")
    else:
        print("Invalid choice")