from pessoa import Pessoa

maria = Pessoa('Maria', 5, 20, 100,'F')
joao = Pessoa('João', 12, 40, 140, 'M')
pedro = Pessoa('Pedro', 22, 65, 170, 'M')
bia = Pessoa('Bia', 18, 55, 160, 'F')
julia = Pessoa('Julia', 30, 65, 170, 'F')
carlos = Pessoa('Carlos', 2, 11, 80, 'M')
jonas = Pessoa('Jonas', 34, 70, 180, 'M')

maria.idade = 10
maria.aniversario()

pedro.crescer(2)

bia.casar(carlos)

pedro.casar(maria)
# pedro.__estado_civil = 'casado(a)'  # burla
pedro.casar(julia)
pedro.casar(bia)

maria.morrer()
maria.engordar()

bia.casar(jonas)
bia.morrer()

pedro.morrer()

jonas.casar(julia)