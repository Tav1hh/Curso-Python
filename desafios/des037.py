# Escreva um programa que leia um número inteiro qualquer e peça para o úsuario escolher qual será a Base da Conversão
# 1 - Decimal
# 2 - Octal
# 3 - Hexadecimal
import decimal

print("\033[33m=\033[m"*20)
n = int(input("Digite um número: "))
print("1 - Decimal")
print("2 - Octal")
print("3 - Hexadecimal")
print("4 - Binario")
opt = int(input("Escolha uma opção: "))
print("\033[33m=\033[m"*20)

b = bin(n)

if opt == 1:
    print("O número {} na base \033[33mDECIMAL\033[m fica {}".format(n,int(b,10)))
elif opt == 2:
    print("O número {} na base \033[33mOCTAL\033[m fica {}".format(n,int(b,8)))
elif opt == 3:
    print("O número {} na base \033[33mHEXADECIMAL\033[m fica {}".format(n,int(b,16)))
elif opt == 4:
    print("O número {} na base \033[33mBINARIA\033[m fica {}".format(n,int(b,2)))