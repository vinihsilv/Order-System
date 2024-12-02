class Produto():
    produtos = []
    def __init__(self,nome,id_produto,preco,estoque):
        self.nome = nome 
        self.id_produto = id_produto 
        self.preco = preco
        self.estoque = estoque

    @classmethod
    def adicionar_produto(cls,Produto):
        cls.produtos.append({
            'id_produto': Produto.id_produto,
            'nome': Produto.nome,
            'preco': Produto.preco,
            'estoque': Produto.estoque
        })
        print(f"Produto {Produto.nome} adicionado com sucesso!")

    @classmethod
    def gerar_relatorio_produtos(csl,produto):
        for produto in csl.produtos:
            print(f"ID Produto: {produto['id_produto']}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Estoque: {produto['estoque']}") 