class Vertice:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def __str__(self):
        return "Vértice %i" % self.id