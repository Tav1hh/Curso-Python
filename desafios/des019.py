# Sorteia um dos 4 alunos para apagar o quadro
from random import choice
a1 = input("Aluno 1: ")
a2 = input("Aluno 2: ")
a3 = input("Aluno 3: ")
a4 = input("Aluno 4: ")
lista = [a1,a2,a3,a4]
sorteado = choice(lista)
print("O aluno sorteado é {}".format(sorteado))
