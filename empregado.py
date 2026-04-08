# Nomes dos componentes da atividade:
# João Henrique e Daniel Henry

class empregado:
    def __init__(self, nome, cpf, salario):
        self.nome = nome 
        self.cpf = cpf
        self.salario = salario

    def setNome(self, nome):
        self.nome = nome 
        
    def getNome(self):
        return self.nome
    
    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf
    
    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario
    
    def calcularDesconto(self):
        if self.salario > 8000.00:
            desconto = (35 / 100) * self.salario
            salarioNovo = self.salario - desconto
            self.salario = salarioNovo
            print(f'O valor do seu desconto é', desconto)
        
        elif self.salario >= 4000.00 and self.salario < 8000.00:
            desconto = (30 / 100) * self.salario
            salarioNovo = self.salario - desconto
            self.salario = salarioNovo
            print(f'O valor do seu desconto é', desconto)

        elif self.salario < 4000.00:
            desconto = (20 / 100) * self.salario
            salarioNovo = self.salario - desconto
            self.salario = salarioNovo
            print(f'O valor do seu desconto é', desconto)
    
class TestarEmpregado:
    def main():
        nome = input('Digite seu nome: ')
        cpf = int(input('Digite seu CPF: '))
        salario = float(input('Digite seu salário: '))

        trabalhador = empregado(nome, cpf, salario)

        print('Nome:', trabalhador.getNome())
        print('CPF:', trabalhador.getCpf())
        print('Salário:', trabalhador.getSalario())

        trabalhador.calcularDesconto()

        print('Seu novo salário pós desconto:', trabalhador.getSalario())

        mudarSalario = float(input('Adicione um novo salário: '))
        trabalhador.setSalario(mudarSalario)
        print('Seu novo salário: ', trabalhador.getSalario())

TestarEmpregado.main()

 # maneira que utilizamos para fazer os testes dos metodos
 # obs: ajuda de rafael joaquim. Ele pediu para falar com vincente para sabe se ele pode gmhar alguns pontos extra.      
'''
sla = empregado('', '', 0.0)

nome = input('qual seu nome, seu falido: ')
sla.setNome(nome)

cpf = input('Qual o cpf do neymar: ')
sla.setCpf(cpf)

salario = float(input('Diga o seu salario seu morador de baixo da ponte: '))
sla.setSalario(salario)

print('nome:', sla.getNome())
print('cpf:', sla.getCpf())
print('salario:', sla.getSalario())

sla.calcularDesconto()
print('seu novo salario pos desconto:', sla.getSalario())'''