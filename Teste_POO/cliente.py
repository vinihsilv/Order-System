class Cliente():
    clientes = []
    def __init__(self, nome,email,id_cliente):
        self.nome = nome 
        self.email = email 
        self.id_cliente = id_cliente
        Cliente.adicionar_cliente(self)


    @classmethod
    def adicionar_cliente(cls, cliente):
        cls.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso!\n")


   
            