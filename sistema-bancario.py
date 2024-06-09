import textwrap
from datetime import datetime

class Transacao:
    def registrar(self, conta):
        pass

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "2347"
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        print("Saque realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return False
        self.saldo += valor
        print("Depósito realizado com sucesso.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários excedido.")
            return False
        if valor > self.limite:
            print("Valor de saque excede o limite da conta.")
            return False
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.saques_realizados += 1
        print("Saque realizado com sucesso.")
        return True

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.transacoes.append({"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": data})

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

def menu(cliente, conta):
    while True:
        acao = input('''\nEnvie
                    'd' para depósito
                    's' para saque
                    'e' para extrato
                    'q' para sair
                ''').strip().lower()

        if acao == "d":
            valor = float(input('Qual valor para depósito? '))
            deposito = Deposito(valor)
            cliente.realizar_transacao(conta, deposito)
        elif acao == "s":
            valor = float(input('Qual valor para saque? '))
            saque = Saque(valor)
            cliente.realizar_transacao(conta, saque)
        elif acao == "e":
            print(conta.historico.transacoes)
        elif acao == 'q':
            break
        else:
            print("Ação inválida. Por favor, envie 'd', 's', 'e' ou 'q'.")
