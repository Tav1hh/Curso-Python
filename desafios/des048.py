# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 e 500.abs
num = 0
for c in range(0,501):
    if c%2 == 1 and c%3 == 0:
        num += c
print("A soma de todos os números entre 0 e 500 é {}".format(num))
