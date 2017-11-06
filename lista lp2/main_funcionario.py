from funcionarios import Funcionario
nome = input('digite o nome do seu funcionario : \n')
funcionario = Funcionario(nome,5000)
porcentagem = float(input('digite a porcentagem do aumento do funcionario : {} \n'.format(funcionario.nome)))
funcionario.aumento_salario (porcentagem)
print('o salario atual de {} depois do aumento é de : {}'.format(funcionario.nome, funcionario.salario))