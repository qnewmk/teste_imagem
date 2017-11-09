dicionario = {}
with open('nota_alunos.txt') as arquivo:
    for linha in arquivo:
        linha = linha.split()
        dicionario.append{linha[0]:linha[1],linha[2]}