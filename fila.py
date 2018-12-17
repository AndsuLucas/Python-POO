class Clientes(object):
    def __init__(self,codigo):
        self.cliente_codigo = codigo



class Caixa(object):
    def __init__(self):
        self.fila = []

    def entrar (self, cliente_codigo):
       self.fila.append(cliente_codigo)

    def sair (self):
        
        while len(self.fila)>0:
            print(self.fila[0],"saindo..")
            self.fila.pop(0)

#simulaçao de pessoas entrando em filas
caixa1 = Caixa()

for cod in range(0,10):
    cliente = Clientes(cod)
    caixa1.entrar(cliente.cliente_codigo)


caixa1.sair()
