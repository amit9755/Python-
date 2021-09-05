class shape:
    #calling constructor
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color
    #instance method
    def finEdge(self):
        return  self.edge
    #instance method
    def modifyEdge(self, newedge):
        self.newedge = newedge

circle = shape(23, "red")
square = shape(33, "blue")
print("no of edge for circle: {}".format(circle.finEdge()))
circle.modifyEdge(56)
print("no of edge for circle: {}".format(square.finEdge()))




