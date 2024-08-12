#Receber notas e calcular a média entre elas

#Declaração de variáveis

n1    = 0.0
n2    = 0.0
n3    = 0.0
soma  = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota "))
soma = n1 + n2 + n3
media = soma/3

print("A média é: ", media)