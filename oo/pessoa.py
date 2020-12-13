class Pessoa:
    def __init__(self, nome=None, idade=33):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Gleibson', 36)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
