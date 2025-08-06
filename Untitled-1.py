class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def get_saldo(self):
        return self.__saldo

# Criando um objeto da classe ContaBancaria
minha_conta = ContaBancaria("João", 1000)

# Realizando operações
minha_conta.depositar(500)
minha_conta.sacar(200)
print(f"Saldo atual da conta do João: R${minha_conta.get_saldo():.2f}")

# Tentativa de acesso direto ao atributo privado (gera erro)
# print(minha_conta.__saldo)  # Descomente esta linha para ver o erro












