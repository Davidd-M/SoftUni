class Circle:
    __PI = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * self.__PI * self.radius

    def calculate_area(self):
        area = self.__PI * (self.radius ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.__PI * (self.radius ** 2)


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")