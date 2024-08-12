#Transforma uma temperatura em Celsius para Fahrenheit e vice e versa

print("Celsius ou Fahrenheit?")
escala = input("Digite a escala inicial:")

if escala in ["Celsius", "celsius"]:
    C = float(input("Digite a temperatura em Celsius:"))
    F = (C * 9 + 160) / 5
    print("A temperatura em Fahrenheit é:", round(F, 2), "Fahrenheit")
elif escala in ["Fahrenheit", "fahrenheit"]:
    F = float(input("Digite a temperatura em Fahrenheit:"))
    C = (F - 32) * 5/9
    print("A temperatura em Celsius é:", round(C, 2), "Celsius")
else:
    print("Apenas para Fahrenheit e Celsius")
