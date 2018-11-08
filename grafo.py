from vertice import Vertice
from aresta import Aresta



class Grafo():
    def __init__(self, direcionado = False):
        self.listaVertices = []
        self.listaArestas = []
        self.direcionado = direcionado
    
    def insereVertice(self,idVertice):
        """
    insere um vértice no grafo

    Args:
        idVertice (string): id do vértice para ser adicionado

        """
        #cria um novo vértice e adiciona no vetor
        self.listaVertices.append(Vertice(idVertice))

    def insereAresta(self, idVerticeOrigem, idVerticeDestino):
        """
    insere uma aresta no grafo, verificando se os vértices existem

    Args:
        idVerticeOrigem (string): id do vértice de origem da aresta
        idVerticeDestino (string): id do vértice de destino da aresta
    Returns:
        bool: True caso consiga ser feita a criação da aresta, e false caso contrário
        """
        v1 = self.buscaVertice(idVerticeOrigem)
        v2 = self.buscaVertice(idVerticeDestino)

        if(v1 == None or v2 == None):
            print("ERRO!:Algum vértice inválido")
            return False
        
        self.listaArestas.append(Aresta(v1,v2))
        return True


    
    def buscaVertice(self, idVertice):
        """
    busca o vértice na lista

    Args:
        idVertice (string): id do vértice para ser localizado

    Returns:
        Vertice: Vértice encontrado ou None, caso não encontre
        """
        for v in self.listaVertices:
            if v.id == idVertice:
                return v
        return None

    def buscaAresta(self, origem, destino):
        """
    busca uma aresta na lista

    Args:
        origem (string): id do vértice de origem para ser localizado
        destino (string): id do vértice de destino para ser localizado

    Returns:
        Aresta: Aresta encontrado ou None, caso não encontre
        """
        for a in self.listaArestas:
            if (a.getOrigem().id == origem) and (a.getDestino().id == destino):
                return a
        return None


    def __str__(self):
        stringR = "GRAFO\n\n"
        stringR += "VÉRTICES\n"

        for v in self.listaVertices:
            stringR += v.__str__()
            stringR += "  "
        
        stringR += "\n\nARESTAS:\n"
        for a in self.listaArestas:
            stringR += a.__str__()
            stringR += "\n"
        return stringR
    
    def buscaLargura(self, vertice):
        for v in self.listaVertices:
            v.cor = "B"        # branco: ainda não foi visitado,
                               # cinza já foi visitado mas ainda não terminou o processo, 
                               # preto: já foi visitado e terminou o processo
            v.pred = None

g = Grafo()
g.insereVertice("MARIA")
g.insereVertice("PEDRO")
g.insereVertice("JOANA")
g.insereVertice("LUIZ")

g.insereAresta("MARIA","PEDRO")
g.insereAresta("MARIA","JOANA")
g.insereAresta("PEDRO","JOANA")
g.insereAresta("PEDRO","LUIZ")

print(g.buscaAresta("MARIA", "PEDRO"))
# g.bus
# g.buscaLargura("MARIA")
g.busca

print(g)

