class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def aumento_salario (self, porcentagem):
        self.salario = float(porcentagem/100.0*self.salario)+self.salario