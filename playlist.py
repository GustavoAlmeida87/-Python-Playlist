class Programa:

    # Função construtora - cria os objetos e atributos da classe.
    # Um _ antes do atributo é para mostrar para outros Devs. que aquele atributo é privado e não deve ser alterado.
    # Um atributo com um _ não é tão privado como com dois __.
    # Pórem é melhor para se usar em herança. Pois, evita problema que podem ocorrer no futuro do programa.
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Método para mostar o valor de um atributo - mesmo que atributo seja privado.
    # Seria os Get de outras linguagens de programação.
    @property
    def likes(self):
        return self._likes

    # Método para dar likes para series e filmes.
    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    # Método para alterar o valor de um atributo - mesmo que atributo seja privado.
    # Seria os Set de outras linguagens de programação.
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Métodos especiais - serve para mostrar uma string com os valores dos atributos do objeto da classe.
    # É uma boa prática quando quiser mostrar algo para o usuário.
    # OBS: cada método especial tem a sua sintaxe e propriedade únicas.
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} Likes: {self.likes}'


# Sintaxe de herança - como criar uma classe que herda métodos e atibutos de outra classe.
class Filme(Programa):

    # super() - é uma sintaxe em python para a classe filha herdar os atributos da classe mãe.
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Métodos especiais - faz com que o atributo de um objeto tenha algumas funçoes de uma lista.
    # OBS: cada método especial tem a sua sintaxe e propriedade únicas.
    def __getitem__(self, item):
        return self._programas[item]

    # Métodos especiais - faz com que o atributo de um objeto tenha suporte a funçoes len.
    # OBS: cada método especial tem a sua sintaxe e propriedade únicas.
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


def main():

    print("Bem vindo ao criador de Playlist de filmes e series!")

    nome_playlist = input("Qual o nome de sua playlist: ")
    lista_de_programas = []

    while True:

        programa = input("Digíte: F -> para adicionar um filme ou S -> para adicionar uma serie: ")
        programa = programa.strip().upper()

        if programa == "F":
            nome_filme = input("Qual o nome do filme: ")
            ano_filme = input("Qual o ano do filme: ")
            duracao_fime = input("Qual a duração do filme: ")
            filme = Filme(nome_filme, ano_filme, duracao_fime)
            lista_de_programas.append(filme)

        elif programa == "S":
            nome_serie = input("Qual o nome da serie: ")
            ano_serie = input("Qual o ano da serie: ")
            temporada_serie = input("Quantas temporadas tem a serie: ")
            serie = Filme(nome_serie, ano_serie, temporada_serie)
            lista_de_programas.append(serie)
        else:
            print("Opcão ínválida")
            continue

        if adicionar_programa():
            continue
        else:
            break

    minha_playlist = Playlist(nome_playlist, lista_de_programas)

    print(f'Playlist: {nome_playlist}')
    for programa in minha_playlist:
        print(programa)

    print(f'Essa Playlist tem {len(minha_playlist)} programas.')


def adicionar_programa():

    while True:
        outro_programa = input("Gostaria de adicionar outro programa: y -> sim ou N -> Não: ")
        outro_programa = outro_programa.strip().upper()

        if outro_programa == "Y":
            return True
        elif outro_programa == "N":
            return False
        else:
            print("Opcão ínválida")
            continue


if __name__ == "__main__":
   main()
