class Carro:
    def __init__(self, proprietario, modelo, cor, placa, preco, marca):
        self.proprietario= proprietario
        self.modelo=modelo
        self.cor=cor
        self.placa=placa
        self.preco=preco
        self.marca=marca
# salvamos uma class denominada Carro (lembrete letra maiúscula), depois disso chamamos uma função, nela vale ressaltar o self(
    def __str__(self):
        return(f'Olá {self.proprietario}, tudo bem?, seu carro é {self.modelo} a cor dele é {self.cor} a placa é de {self.placa} e o preço {self.preco}. Sua marca {self.marca}')

meu_carro= Carro(
        proprietario='Matheus',
        modelo='Siena',
        cor='Preto',
        placa='MFS-3405',
        preco='30000',
        marca='Fiat'
)

print(meu_carro)