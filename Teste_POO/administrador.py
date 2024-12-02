from cliente import Cliente
from produto import Produto
from pedido import Pedido
class Administrador():
    def __init__(self, id_administrador):
        self.id_administrador = id_administrador
        
        
        
   
    def gerar_relatorios_clientes(cls):
        """Gera um relatório com informações de todos os clientes."""
        clientes = Cliente.clientes  
        if not clientes:
            print("Nenhum cliente registrado.\n")
            return
        
        print("Relatório de Clientes:\n")
        for cliente in clientes:
            print(f"ID Cliente: {cliente.id_cliente}, Nome: {cliente.nome}, Email: {cliente.email}\n")

    
    def gerar_relatorio_produtos(cls):
        produtos = Produto.produtos
        if not produtos:
            print("nenhum produto cadastrado\n")
            return
        for produto in produtos:
            print(f"ID Produto: {produto.id_produto}, Nome: {produto.nome}, Preço: R${produto.preco}, Estoque: {produto.estoque}\n")

    def gerar_relatorio_pedidos(cls):
        pedidos = Pedido.pedidos
        if not pedidos:
            print("nenhum pedido cadastrado\n")
            return
        for pedido in pedidos:
            print(f"ID Pedido: {pedido.id_pedido}, id_cliente: {pedido.cliente.id_cliente}, itens {pedido.itens}, status: {pedido.status}\n")
        
        