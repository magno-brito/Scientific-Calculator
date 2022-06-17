from TwoD_shapes import twoD_shapes
class Prism(twoD_shapes):
    def __init__(self, shape , width,):
        super().__init__(shape.turtle,shape.sides,shape.length)
        self.width = width
        self.shape = shape
        self.list_edge = shape.get_list_coordinates()
    def draw3Dshape(self):
        self.shape.draw()
        for i in range(len(self.list_edge)):
            self.shape.turtle.penup()
            self.shape.turtle.goto(self.list_edge[i][0],self.list_edge[i][1])
            self.shape.turtle.pendown()
            self.shape.turtle.left(30)
            self.shape.turtle.forward(self.width)
            self.shape.turtle.right(30)
        self.shape.draw()
    