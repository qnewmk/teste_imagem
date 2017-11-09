dic = {}
#ler arquivo e fechar ao finalizar
with open('tweets.txt') as arquivo:
    #para cadalinha do arquivo
    for linha in arquivo:
        #remove \n da linha
        linha = linha.rstrip()
        #separa a linha por espaços
        palavras = linha.split(' ')
        #percorrer palavras para contar
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1
with open('saida.txt', 'w') as arquivo:
    for chave,valor in dic.items():
        arquivo.write(chave+':'+str(valor)+'\n')