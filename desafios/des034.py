# Aplica um aumento de 10% para salarios acima de 1250 e aumento de 10% para salarios abaixo.
salario = float(input("Salario: "))
if salario > 1250:
    aumento = 10
    salario = salario * aumento / 100 + salario
else:
    aumento = 15
    salario = salario * aumento / 100 + salario
print("Aumento de {}%, novo sálario R${:.2f}".format(aumento,salario))