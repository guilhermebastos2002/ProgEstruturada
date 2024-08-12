#Calcular IMC
from turtle import onclick

#Declaração de variáveis

peso = 0.0
altura = 0.0
IMC = 0.0

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/altura**2

if IMC <= 14.5:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Desnutrição")

if IMC >= 14.5 and IMC <= 20:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Peso Abaixo do Normal")

if IMC >= 20 and IMC <= 24.9:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Peso Normal")

if IMC >= 25 and IMC <= 29.9:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Sobrepeso")

if IMC >= 30 and IMC <= 39.9:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Obesidade")

if IMC >= 40:
    print("Seu IMC é:", round(IMC, 2))
    print("Você faz parte da categoria: Obesidade mórbida")
