
class Cozinha(object):
    def __init__(self):
        self.forno = []
        self.pedido = []

    def recebimento_dos_pedidos(self,  pedido):

        self.pedido.append(pedido)

    def colocar_no_forno(self):

        for p in range(0, len(self.pedido)):

            self.forno.append(self.pedido[p])

    def assar(self):

        c = 1
        while len(self.forno) > 0:
            c += 1
            print(f'Assando o pedido número {c},{self.forno[0]}')
            self.forno.pop(0)


class RegistradorDePedidos(object):
    def __init__(self):
        self.pedidos_registro = []

    def registar(self):

        self.numero = int(input('Insira o número de pedidos:'))
        for num in range(0, self.numero):
            self.pedido = input('Insira o pedido')
            self.pedidos_registro.append(self.pedido)


pedidos = RegistradorDePedidos()
cozinheiro = Cozinha()

pedidos.registar()

for c in range(0, len(pedidos.pedidos_registro)):

    cozinheiro.recebimento_dos_pedidos(pedidos.pedidos_registro[c])

cozinheiro.colocar_no_forno()

cozinheiro.assar()
