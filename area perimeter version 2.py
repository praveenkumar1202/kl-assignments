import math


# importing math module for mathmetical calculation

class CalculateArea:
    """created a class to calculate the area of different shapes"""

    def area_square(self):
        return pow(int(input("Square area: ")), 2)

    def area_rectangle(self):
        return int(input("Rectangle length: ")) * int(input("Rectangle breadth: "))

    def area_triangle(self):
        return 0.5 * int(input("Triangle base: ")) * int(input("Triangle height: "))

    def area_circle(self):
        return math.pi * pow(int(input("Circle radius: ")), 2)

    def area_parallelogram(self):
        return int(input("Parallelogram breadth: ")) * int(input("Parallelogram height: "))


class CalculatePerimeter:
    """created a class to calculate the perimeter of different shapes"""

    def perimeter_square(self):
        return 4 * int(input("Square side: "))

    def perimeter_rectangle(self):
        return 2 * (int(input("Rectangle length: ")) + int(input("Rectangle breadth: ")))

    def perimeter_triangle(self):
        return 3 * int(input("Triangle side: "))

    def perimeter_circle(self):
        return 2 * math.pi * int(input("Circle radius: "))

    def perimeter_parallelogram(self):
        return 2 * (int(input("Parallelogram breadth: ")) + int(input("Parallelogram side: ")))


# main function
def main():
    display = """
        Select a shape:
        1. Square
        2. Rectangle
        3. Triangle
        4. Circle
        5. Parallelogram
        6. Quit
    """

    options = """
        Select an option:
        1. Calculate Area
        2. Calculate Perimeter
    """

    area_object = CalculateArea()
    perimeter_object = CalculatePerimeter()
    """ creating objects for class area and perimeter"""

    while True:
        print(display)
        shape_choice = int(
            input("Enter your choice (1/2/3/4/5/6): "))  # getting an input from an user to specify the shapes

        if shape_choice == 6:
            break

        print(options)
        display_choice = int(input("Enter your choice (1/2): "))

        if display_choice == 1:

            if shape_choice == 1:
                print(area_object.area_square())
            elif shape_choice == 2:
                print(area_object.area_rectangle())
            elif shape_choice == 3:
                print(area_object.area_triangle())
            elif shape_choice == 4:
                print(area_object.area_circle())
            elif shape_choice == 5:
                print(area_object.area_parallelogram())
            else:
                print("Invalid choice")

        elif display_choice == 2:

            if shape_choice == 1:
                print(perimeter_object.perimeter_square())
            elif shape_choice == 2:
                print(perimeter_object.perimeter_rectangle())
            elif shape_choice == 3:
                print(perimeter_object.perimeter_triangle())
            elif shape_choice == 4:
                print(perimeter_object.perimeter_circle())
            elif shape_choice == 5:
                print(perimeter_object.perimeter_parallelogram())
            else:
                print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()  # calling main function
