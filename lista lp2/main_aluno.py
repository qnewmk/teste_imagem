from alunos import Aluno

nome = 'kaio'
curso = 'S.I'
tempo = '12'
aluno = Aluno (nome, curso, tempo)
print('o aluno {} está {} horas em dormir'.format(aluno.nome,aluno.tempo_sem_dormir))