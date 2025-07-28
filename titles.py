from turtle import Turtle

class Titles():

    def __init__(self):
        self.titles: Turtle = []

    def add_title(self, x, y, title):
        print(f"{x}, {y}, {title}")
        obj = Turtle()
        obj.color("black")
        obj.goto((x, y))
        obj.write(title, False, "center", ("Arial", 15, "bold"))
        self.titles.append(obj)
