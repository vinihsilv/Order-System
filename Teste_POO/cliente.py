class Cliente():
    clientes = []
    def __init__(self, nome,email,id_cliente):
        self.nome = nome 
        self.email = email 
        self.id_cliente = id_cliente


    @classmethod
    def adicionar_cliente(cls, cliente):
        cls.clientes.append({
            'id_cliente': cliente.id_cliente,
            'nome': cliente.nome,
            'email': cliente.email
        })
        print(f"Cliente {cliente.nome} adicionado com sucesso!")
        


    @classmethod
    def gerar_relatorios_clientes(cls, cliente):
        for cliente in cls.clientes:
            print(f"ID Cliente: {cliente['id_cliente']}, Nome: {cliente['nome']}, Email: {cliente['email']}")
            