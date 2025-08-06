class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo


    #acelerar o carro
    def acelerar (self, valor):
        self.velocidade_atual += valor
        print(f"O carro acelerou para {self.velocidade_atual} km/h. ")

        #frear o carro
    def frear (self, valor):
        #evitar a velocidade negativa
        if self.velocidade_atual - valor >= 0:
            self.velocidade_atual -= valor
        else:
            self.velocidade_atual = 0
        print(f"O carro freou para {self.velocidade_atual} km/h. ")


    def status(self):
        print("----STATUS DO CARRO----")
        print("Marca: ", f"{self.marca}")
        print("Modelo: ", f"{self.modelo}")
        print("Cor:", f"{self.cor}")
        print("Velocidade atual:", f"{self.velocidade_atual}")
        print("------------------------")
# Criando um carro
meu_carro = Carro("vermelho", "Toyota", "Corolla")

# Definindo velocidade inicial
meu_carro.velocidade_atual = 0

# Acelerando o carro
meu_carro.acelerar(50)

# Freando o carro
meu_carro.frear(20)

# Mostrando o status
meu_carro.status()
