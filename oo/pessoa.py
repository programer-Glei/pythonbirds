class Pessoa:
    def __init__(self, nome=None, idade=33, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = filhos

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pessoa = []
    joaquim = Pessoa('Joaquim')
    maria = Pessoa('Maria')
    jose = Pessoa('Jose',40)
    pessoa.append(joaquim)
    pessoa.append(maria)
    pessoa.append(jose)
    p = Pessoa('Gleibson', 36, pessoa)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    for filo in p.filhos:
        for achei in filo:
            print(f'nome {achei.nome} e idade {achei.idade}')
