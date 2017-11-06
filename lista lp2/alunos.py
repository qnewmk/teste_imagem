class Aluno :

    def __init__(self, nome, curso, tempo):
        self.nome = nome
        self.curso = curso
        self.tempo_sem_dormir =  tempo

    def estudar (self, horas_de_estudo):
        horas_de_estudo = horas_de_estudo + self.tempo_sem_dormir
        self.horas_estudo = horas_de_estudo

    def dormir(self, horas_de_sono):
        self.tempo_sem_dormir = self.tempo_sem_dormir - horas_de_sono