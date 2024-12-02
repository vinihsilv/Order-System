from cliente import Cliente
from produto import Produto
from item_pedido import ItemPedido
from pedido import Pedido
from administrador import Administrador

def main():
    
    produto1 = Produto(101, "Laptop", 3000.00, 10)
    produto2 = Produto(102, "Mouse", 50.00, 20)

    
    cliente1 = Cliente("João Silva", "joao.silva@email.com",1)
    cliente2 = Cliente("lucas Silva", "lucas.silva@email.com",2)

    admin = Administrador(101)

    item1 = ItemPedido(produto1, 2)  
    item2 = ItemPedido(produto2, 1)  

   
    pedido1 = Pedido(1, cliente1, [item1, item2], "Pendente")
    pedido2 = Pedido(2, cliente2, [item1, item2], "Pendente")

    print("Relatório de pedidos antes do processamento:\n")
    admin.gerar_relatorio_pedidos()
    

    Pedido.processar_pedido(1)
    Pedido.processar_pedido(2)

    


    admin.gerar_relatorios_clientes()
    print("\nRelatório de produtos após o processamento dos pedidos:\n")
    admin.gerar_relatorio_produtos()
    print("\nRelatório de pedidos após o processamento:\n")
    admin.gerar_relatorio_pedidos()


if __name__ == "__main__":
    main()