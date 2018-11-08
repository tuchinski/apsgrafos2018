class Vertice():
    def __init__(self,id):
        self.id = id
        self.visitado = False
        self.entrada = 0
        self.saida = 0
        self.cor = 'B'
        self.pred = None

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def __str__(self):
        
        return "%s" % self.id