from produto import Produto

class ItemPedido():
    def __init__(self, produto, quantidade):
        self.produto = produto  
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.preco * self.quantidade

    def __repr__(self):
        return f"ItemPedido({self.produto}, {self.quantidade})"