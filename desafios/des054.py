# Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
menor = 0
for c in range(1,7):
    idade = int(input("Idade {}: ".format(c)))
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print("Das 6 Pessoas, {} são responsaveis e {} não são".format(maior,menor))
