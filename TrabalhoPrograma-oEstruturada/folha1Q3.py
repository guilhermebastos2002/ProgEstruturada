#Programa que lê dois valores inteiros e troca os valores lidos,
#de forma que, ao final, x contenha o valor de y e y tenha o valor de x

x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
x,y=y,x
print(x,y)
