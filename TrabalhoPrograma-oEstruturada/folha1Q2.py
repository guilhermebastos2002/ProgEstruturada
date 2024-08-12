#Sistema que recebe 3 valores inteiros e mostra a soma de seus inversos

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
somainv = 1/n1 + 1/n2 + 1/n3

print("A soma do inverso desses números é:", round(somainv, 2))