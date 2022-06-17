class twoD_shapes:
    def __init__(self, turtle, sides,length):
        self.turtle = turtle
        self.sides = sides
        self.length = length
        self.inter_angulum = (sides-2)*180/sides
        self.list_of_coordinates = []
    def draw(self):
        for i in range(self.sides):
            self.turtle.forward(self.length)
            self.turtle.left(180-self.inter_angulum)
            self.list_of_coordinates.append([self.turtle.xcor(),self.turtle.ycor()])
        
    def get_list_coordinates(self):
        return self.list_of_coordinates
        

