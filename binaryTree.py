class Node(object):
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def addNode(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._addNode(valor, self.root)

    def _addNode(self, valor, currentNode):
        if valor < currentNode.valor:
            if currentNode.esquerda == None:
                currentNode.esquerda = Node(valor)
            else:
                self._addNode(valor, currentNode.esquerda)
        elif valor > currentNode.valor:
            if currentNode.direita == None:
                currentNode.direita = Node(valor)
            else:
                self._addNode(valor, currentNode.direita)
        else:
            print('O valor já está na arvore')

    def altura(self, node):
        if node == None:
            return 0
        alturaEsquerda = self.altura(node.esquerda)
        alturaDireita = self.altura(node.direita)
        return 1 + max(alturaEsquerda, alturaDireita)


tree=BinaryTree()
tree.addNode(3)
tree.addNode(9)
tree.addNode(20)
tree.addNode(15)
tree.addNode(7)
print(tree.altura(tree.root))
