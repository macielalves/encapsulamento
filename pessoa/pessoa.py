from doctest import run_docstring_examples


class Pessoa:
    def __init__(
            self,
            nome,
            idade,
            peso,
            altura,
            sexo,
            estado="vivo",
            estado_civil="solteiro",
            conjuge=None
        ):
        """A classe Pessoa ...

        Atributos:
            nome (str): Nome da Pessoa
            idade (int): Quantidade de anos
            peso (float): valor em Kg
            altura (float): valor em cm
            sexo (str): [M]asculino, [F]eminino
            estado (str): [v]ivo, [m]orto
            estado_civil (str): 'solteiro', 'casado', viúvo
            conjuge (object): Um objeto Pessoa()
        """
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def peso(self):
        return self.__peso
    @property
    def altura(self):
        return self.__altura
    @property
    def sexo(self):
        return self.__sexo
    @property
    def estado(self):
        return self.__estado
    @property
    def estado_civil(self):
        return self.__estado_civil
    @property
    def conjuge(self):
        return self.__conjuge
    # start warning
    @property
    def __no_access(self):
        print("Sem permissão")
    # @__no_access.setter
    # def f(self, txt):
    #     print("Sem permissão para alterar")
    # end warning
    @nome.setter
    def nome(self, txt):self.__no_access
    @idade.setter
    def idade(self, txt):self.__no_access
    @peso.setter
    def peso(self, txt):self.__no_access
    @altura.setter
    def altura(self, txt):self.__no_access
    @sexo.setter
    def sexo(self, txt):self.__no_access
    @estado.setter
    def estado(self, txt):self.__no_access
    @estado_civil.setter
    def estado_civil(self, txt):self.__no_access
    @conjuge.setter
    def conjuge(self, txt):self.__no_access

    def envelhecer(self):
        if self.__idade <= 21:
            self.__altura += 0.5  # Cresce 0,5 a cada ano 
        self.__idade += 1  # Envelhece um ano
    
    def engordar(self, peso):
        try:self.__peso += peso if peso > 0 else 0
        except Exception as e:print(e)

    def emagrecer(self, peso):
        try:self.__peso -= abs(peso)
        except Exception as e:print(e)
    
    def crescer(self, altura):
        if self.idade <= 21:
            self.__altura += altura
    
    def requisitos_casamento(self, p1, p2):
        if p1.estado == 'vivo' and p1.idade >= 18:
            if p2.estado == 'vivo' and p2.idade >= 18:
                return True
    
    def casar(self, conjuge):
        if self.requisitos_casamento(self, conjuge):
            self.__estado_civil = 'casado(a)'
            print(f'{self.nome} casou-se com {conjuge.nome}!')

    def morrer(self):
        self.__estado = 'morto'

    def __str__(self):
        return f'nome: {self.nome}, estado civíl: {self.estado_civil}, idade: {self.idade}, vivo/morto: {self.estado}, peso: {self.peso}Kg, altura: {self.altura / 100}m'