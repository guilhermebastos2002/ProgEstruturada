#Programa que recebe uma medida em polegadas e transforma em milímetros e vice e versa

print("Polegadas ou Milímetros?")
uni_med = input("Digite a unidade de medida inicial:")

if uni_med in ["Polegadas", "polegadas", "polegada", "Polegada"]:
    P = float(input("Digite a medida em polegadas:"))
    MM = P * 25.4
    print("A medida em Milímetros é:", round(MM, 2), "Milímetros")

elif uni_med in ["Milímetros", "milímetros", "milímetro", "Milímetro"]:
    MM = float(input("Digite a medida em Milímetros:"))
    P = MM / 25.4
    print("A medida em Polegadas é:", round(P, 2), "Polegadas")

else:
    print("Apenas para Polegadas e Milímetros.")



