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
        if self.is_alive:
            return self.__idade
        else:
            return f'{self.nome} está mort{"a"if self.sexo.upper()=="F"else "o"}'
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
    def __morreu(self):
         print(f"Operação não realizada. {self.nome} está mort{'o'if self.sexo.upper() == 'M'else 'a'}")
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
            print(f"{self.nome} ainda está viv{'a'if self.sexo.upper() == 'F'else 'o'}!")

    def aniversario(self):
        print(f"{self.nome} está com {self.idade} anos e {self.altura} cm de altura")

    def envelhecer(self):
        if self.is_alive:
            if self.__idade < 21:
                self.__altura += 5  # Cresce 5cm a cada execução se idade menor que 21
            self.__idade += 1  # Envelhece um ano
    
    def pronomes(self):
        if self.sexo.upper() == 'M':
            return 'ele/dele'
        elif self.sexo.upper() == 'F':
            return 'ela/dela'
        return 'Tanque de guerra'
    
    def engordar(self, peso=0):
        if self.is_alive:
            try:self.__peso += peso if peso > 0 else 0
            except Exception as e:print(e)
        else:
            self.__morreu()

    def emagrecer(self, peso):
        if self.is_alive:
            try:self.__peso -= abs(peso)
            except Exception as e:print(e)
        else:
            self.__morreu()
    
    def crescer(self, altura):
        if self.is_alive:
            if self.idade <= 21:
                self.__altura += altura
            else:
                print(f"{self.nome} não pode mais crescer pois está com 21 anos ou mais")
    
    def pode_casar(self):
        if self.is_alive and self.idade >= 18 and 'casado' not in self.estado_civil:
            return True
        else:
            if self.is_alive and self.idade < 18:
                print(f"Casamento não permitido. {self.nome} é de menor.")
            elif self.is_alive and 'casado' in self.estado_civil:
                print(f"Casamento não realizado. {self.nome} é casado.")
    
    def casar(self, conjuge=None):
        if self.is_alive:
            if conjuge is not None and self.pode_casar() and conjuge.pode_casar():
                self.__conjuge = conjuge
                self.__estado_civil = 'casado(a)'
                self.__conjuge.__estado_civil = 'casado(a)'
                self.__conjuge.__conjuge = self
                print(f'{self.nome} está casado com {self.__conjuge.nome}!')
        else:
            self.__morreu()

    def morrer(self):
        if self.is_alive:
            self.__estado = 'morto'
            print(f'{self.nome} morreu!')
            if self.__conjuge is not None:
                try:
                    self.__conjuge.__estado_civil = f"viúv{'a'if self.__conjuge.sexo.upper() == 'F' else 'o'}"  # -*- atenção -*-
                    print(f"{self.__conjuge.nome} ficou {self.__conjuge.estado_civil}")
                    self.__conjuge = None
                except Exception as e:
                    print('Um alienígena?')
                    print(e)
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
        else:
            print("Ainda ta cedo pra tentar reviver!")

    def __str__(self):
        return f'nome: {self.nome}, estado civíl: {self.estado_civil}, idade: {self.idade}, vivo/morto: {self.estado}, peso: {self.peso}Kg, altura: {self.altura / 100}m'