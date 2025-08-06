"""
A class for representing a circle
"""


class circle():
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        print(f"Circumference is equal to {2 * 3.14 * self.radius} units")

    def display_area(self):
        print(f"Area is equal to {3.14 * self.radius ** 2} units")


new_circle = circle(4)
new_circle.display_area()
new_circle.display_circumference()