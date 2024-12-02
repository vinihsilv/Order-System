

class ItemPedido():
    def __init__(self, produto, quantidade):
        self.produto = produto  
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.preco * self.quantidade

    def __repr__(self):
        return f"id do produto: {self.produto}, quantidade: {self.quantidade} "