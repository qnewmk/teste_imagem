linha = []
with open('animais.txt') as arquivo:
    for linha in arquivo:
        linhas= linha.rstrip()
        palavras = linha.split()
        palavras.sort()
        print(palavras)