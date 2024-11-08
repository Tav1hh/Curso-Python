# Um programa que lé o ano e diz se ele e bissexto
ano = str(input("Ano: "))
if int(ano[-2:])%4 == 0:
    if int(ano) >= 400:
        if int(ano) % 400 == 0:
            print("Ano Bissexto!")
        else:
            print("Ano Normal!")
    else:
        print("Ano Bissexto!")

else:
    print("Ano Normal!")
