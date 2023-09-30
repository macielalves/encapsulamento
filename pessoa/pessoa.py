from random import seed, choice
seed()


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
            sexo (str): ['M']asculino, ['F']eminino
            estado (str): 'vivo', 'morto'
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
        print("Sem permissão!")
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
        if self.is_alive:
            if self.__idade < 21:
                self.__altura += 5  # Cresce 5cm a cada ano 
            self.__idade += 1  # Envelhece um ano
    
    def pronomes(self):
        if self.sexo.upper() == 'M':
            return 'ele/dele'
        elif self.sexo.upper() == 'F':
            return 'ela/dela'
        return 'Tanque de guerra'

    @property
    def is_alive(self):
        if self.__estado == 'vivo':
            return True
        return False
    @is_alive.setter
    def is_alive(self, txt):
        if 'false' in (a:=str(txt).lower()):
            print(a)
            self.morrer()
        elif self.is_alive:
            print(f"{self.nome} ainda está {self.vivo}!")
    
    def engordar(self, peso):
        if self.is_alive:
            try:self.__peso += peso if peso > 0 else 0
            except Exception as e:print(e)

    def emagrecer(self, peso):
        if self.is_alive:
            try:self.__peso -= abs(peso)
            except Exception as e:print(e)
    
    def crescer(self, altura):
        if self.is_alive:
            if self.idade <= 21:
                self.__altura += altura
    
    def requisitos_casamento(self, p1, p2):
        if p1.is_alive and p1.idade >= 18:
            if p2.is_alive and p2.idade >= 18:
                return True
    
    def casar(self, conjuge):
        if self.is_alive:
            self.__conjuge = conjuge
            if self.requisitos_casamento(self, self.conjuge):
                self.__estado_civil = 'casado(a)'
                print(f'{self.nome} casou-se com {self.conjuge.nome}!')

    def morrer(self):
        if self.is_alive:
            self.__estado = 'morto'
            print(f'{self.nome} morreu!')
        else:
            print(f"{self.nome} ja está morto!")

    @property
    def a(self):
        self.__a = choice(range(0, 1_000, 1))
        return self.__a
    @property
    def b(self):
        self.__b = choice(range(0, 1_000, 1))
        return self.__b
    def reviver(self):
        """Tentar reviver?"""
        if not self.is_alive:
            a = self.a
            b = self.b
            if a == b:
                self.__estado = 'vivo'
            else:
                print('Não foi posível reviver!')

    def __str__(self):
        return f'nome: {self.nome}, estado civíl: {self.estado_civil}, idade: {self.idade}, vivo/morto: {self.estado}, peso: {self.peso}Kg, altura: {self.altura / 100}m'