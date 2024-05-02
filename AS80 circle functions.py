def circle_area(radius):
    pi = 3.14159
    area = pi*(radius**2)
    print ("Area of the circle: ",area) 
    return area

def circle_circumference(radius):
    pi = 3.14159
    circumference = 2*pi*radius
    print ("Circumference of the circle: ",circumference) 
    return circumference


if __name__ == "__main__":
    print ("This program assumes the radius is an integer and the value of pi is taken as 3.14159.\n")
    radius = int(input("What is the radius of the circle: "))
    circle_area(radius)
    circle_circumference(radius)
