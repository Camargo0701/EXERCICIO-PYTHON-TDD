class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome=nome
        self.email=email
        self.rg=rg
        self.idade=idade
        self.salario=salario

    def __str__(self):
         return (f'Olá {self.nome}, você foi com sucesso cadastrado com sucesso!')

    def aumentar_salario(self, salario):
        return self.salario + salario

meu_cadastro = Funcionario(
    nome= 'Matheus',
    email= 'matheus-0701@hotmail.com',
    rg= '54.101.980-6',
    idade= '18',
    salario= 20000
)

print(meu_cadastro.aumentar_salario)
if idade > 45:
