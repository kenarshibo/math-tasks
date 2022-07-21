import math

def compare_coordinates(x, y, r):
    hypotenuse = math.sqrt(x ** 2 + y ** 2)

    if hypotenuse > r:
        print('There is not a coin here.')

    else:
        print('There is a coin here!')


x_coordinate = float(input('Enter the x coordinate: '))
y_coordinate = float(input('Enter the y coordinate: '))
radious = float(input('Enter the radious: '))
compare_coordinates(x_coordinate, y_coordinate, radious)
