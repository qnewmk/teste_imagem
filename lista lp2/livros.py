class Livro:
    def __init__(self, nome , paginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = paginas
        self.autor = autor
        self.preco = preco

    def setpreco(self):
        res = input('deseja alterar o preço do livro {} : (S/N)'.format(self.nome))
        if (res == 's' or res == 'S'):
            print('o preço atual é : {}'.format(self.preco))
            self.preco =input('digite o novo preço : ')
        elif(res == 'n' or res == 'N'):
            print('ok')
            x = 0
            while (x ==0):
                break
    def getpreco(self):
        print('o preço atual do livro {} é R${}'.format(self.nome,self.preco))