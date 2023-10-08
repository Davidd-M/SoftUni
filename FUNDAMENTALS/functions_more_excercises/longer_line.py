import math

def get_distance(_x1, _y1, _x2, _y2):
    return math.sqrt((_x2 - _x1) ** 2 + (_y2 - _y1) ** 2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

dist1 = get_distance(x1, y1, 0, 0)
dist2 = get_distance(x2, y2, 0, 0)
dist3 = get_distance(x3, y3, 0, 0)
dist4 = get_distance(x4, y4, 0, 0)

# Calculate the lengths of both lines
line1_length = dist1 + dist2
line2_length = dist3 + dist4

# Determine which point is closer to the center for both pairs
if dist1 <= dist2:
    closer_point1 = (x1, y1)
    farther_point1 = (x2, y2)
else:
    closer_point1 = (x2, y2)
    farther_point1 = (x1, y1)

if dist3 <= dist4:
    closer_point2 = (x3, y3)
    farther_point2 = (x4, y4)
else:
    closer_point2 = (x4, y4)
    farther_point2 = (x3, y3)

# Compare the lengths and distances to select the result
if line1_length > line2_length or (line1_length == line2_length and dist1 + dist2 <= dist3 + dist4):
    print(f"({int(closer_point1[0])}, {int(closer_point1[1])})({int(farther_point1[0])}, {int(farther_point1[1])})")
else:
    print(f"({int(closer_point2[0])}, {int(closer_point2[1])})({int(farther_point2[0])}, {int(farther_point2[1])})")
