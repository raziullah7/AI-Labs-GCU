import math

# A closed polygon with N sides can be represented as a list of tupils of N connected cooordinates. [(x1,y1), (x2,y2),(x2,y2),(x2,y2)]
# Write a python function that takes a list of N tuples as input and returns the perimeter of the polygon.
# Remember that your code should work for any value of N
# perimeter = sum of all sides
# distance = SQRT((X2 - X1)^2 + (Y2 - Y1)^2)

def distance(p1, p2):
    # distance between two points.
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def polygon_perimeter(vertices):
    # perimeter of a polygon from a list of vertices.
    perimeter = 0
    N = len(vertices)
    for i in range(N):
        perimeter += distance(vertices[i], vertices[(i + 1) % N])
    return perimeter


# main function
vertices = [(0, 0), (0, 1), (1, 1), (1, 0), (2,3), (3,2)]
print("Perimeter:", polygon_perimeter(vertices))
