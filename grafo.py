class Grafo:
    def __init__(self, direcionado = False):
        self.listaVertices = []
        self.listaArestas = []
        self.direcionado = direcionado
    
    def insereVertice(self,idVertice):
        #cria um novo vértice e adiciona no vetor
        self.listaVertices.append(Vertice(id))
