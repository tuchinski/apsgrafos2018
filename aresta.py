class Aresta:
    def __init__(self, origem,destino,peso=0):
        self.origem = origem
        self.destino = destino
        self.peso = peso
    
    def getOrigem(self)
        return self.origem
    
    def getDestino(self)
        return self.destino
    
    def getPeso(self)
        return self.peso
    
    
    def setOrigem(self, origem)
        self.origem = origem
    
    def setDestino(self, destino)
        self.destino = destino

    def setPeso(self, peso)
        self.peso = peso

    def __str__(self):
        return "Aresta(%s---%i--->%s)" % (self.origem, self.peso, self.destino)