class Produto():
    produtos = []
    def __init__(self,nome,id_produto,preco,estoque):
        self.nome = nome 
        self.id_produto = id_produto 
        self.preco = preco
        self.estoque = estoque
        Produto.adicionar_produto(self)

    @classmethod
    def adicionar_produto(cls,produto):
        cls.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado com sucesso!\n")

    def __repr__(self):
        return f"{self.nome} (R${self.preco:.2f})"

    