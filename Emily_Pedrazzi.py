#Emily Pedrazzi
#Function #2
#4-5-24
#CS 162

def rect_solid_area(length, width, height):
    return length * width * height

length = int(input("What is the length of your rectangle?: "))
width = int(input("What is the width of your rectangle?: "))
height = int(input("What is the height of your rectangle?: "))

if(length > 0 and width > 0 and height > 0):
    print("The surface area of your rectangle is",rect_solid_area(length, width, height))
else:
    print("All values must be greater than 0, please try again.")
