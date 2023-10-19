class Point:
    __match_args__ = ('x', 'y')
    def __int__(self, x,y):
        self.x = x
        self.y = y
        
match points:
    case [Point(0, 0)]:
        print("Origin")
    case [Point(x, y)]:
        print(f"x = {x}, y={y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Y axis X={y1}, {y2}")
    case _:
        print("Somewhere else")
# var = 0    
Point(0,0)
# print(Point(1, y=var))
# print(Point(x=1, y=var))
# print(Point(y=var, x=1))