from item_pedido import ItemPedido
from cliente import Cliente

class Pedido():
    pedidos = []
    
    def __init__(self, id_pedido, cliente, itens, status="pendente"):
        self.id_pedido = id_pedido
        self.cliente = cliente 
        self.itens = itens  
        self.status = status

    @classmethod
    def criar_pedido(cls, id_pedido, cliente, itens, status="pendente"):
        pedido = cls(id_pedido, cliente, itens, status)
        cls.pedidos.append(pedido)
        return pedido
    
    @classmethod
    def processar_pedido(cls, id_pedido):
        pedido = None
        for p in cls.pedidos:
            if p.id_pedido == id_pedido:
                pedido = p
                break

        if not pedido:
            print(f"Pedido com ID {id_pedido} não encontrado.")
            return

        total = 0
        for item in pedido.itens:
            produto = item.produto  
            if produto.estoque >= item.quantidade:  
                produto.estoque -= item.quantidade  
                total += produto.preco * item.quantidade  
            else:
                print(f"Estoque insuficiente para o produto {produto.nome}. Pedido não pode ser processado.")
                return

        pedido.status = 'Pago' 
        print(f"Pedido {id_pedido}, status {pedido.status} processado com sucesso. Total a pagar: R${total:.2f}")
        return pedido