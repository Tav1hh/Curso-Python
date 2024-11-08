# O computador escolhe um número de 1 a 5 e o úsuario tenta descobrir
from random import randint
c = randint(1,6)
n = int(input("Escolha um número de 1 a 5: "))
if n == c:
    print("Parabens!! você acertou eu pensei em:",c)
else:
    print("Não foi dessa vez.., eu pensei em:",c)
print("Fim do jogo!")