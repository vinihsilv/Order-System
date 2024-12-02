from cliente import Cliente
from produto import Produto
from item_pedido import ItemPedido
from pedido import Pedido

def main():
    
    produto1 = Produto(101, "Laptop", 3000.00, 10)
    produto2 = Produto(102, "Mouse", 50.00, 20)

    
    cliente1 = Cliente(1, "João Silva", "joao.silva@email.com")

   
    item1 = ItemPedido(produto1, 2)  
    item2 = ItemPedido(produto2, 1)  

   
    pedido1 = Pedido.criar_pedido(1001, cliente1, [item1, item2], "Pendente")

   
    Pedido.processar_pedido(1001)

if __name__ == "__main__":
    main()