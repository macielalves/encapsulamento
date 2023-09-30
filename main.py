from pessoa import Pessoa

p1 = Pessoa('Maria', 23, 45.0, 160,'F')
p2 = Pessoa('Paulo', 25, 59.0, 170, 'M')
p1.envelhecer()
p1.casar(p2)

print(p1.estado_civil)
