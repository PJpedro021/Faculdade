# s) Escreva um algoritmo em Python que leia o número de litros vendidos e o tipo de
# combustível (codificado da seguinte forma: 1 - álcool, 2 - gasolina), calcule e imprima o
# valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o
# preço do litro do álcool é R$ 2,90. Os cálculos finais são definidos de acordo com a tabela
# abaixo: alcoo ate 20 litros 3% de desconto, acima de 20 litros 5% de desconto
# gasolina ate 20 litros 4% de desconto, acima de 20 litros 6% de desconto

print("Compra de combustivel")

combustivel = int(input("Digite  1 - álcool 2 - gasolina : "))
print("----------------")
litros = float(input("Digite a quantidade de combustivel: "))

if (combustivel == 1):
    print("***Alcool***")
    print("----------------")
    valCombustivel = 2.90
    if (litros <= 20):
        desconto = valCombustivel * 0.03
    else:
        desconto = valCombustivel * 0.05

if (combustivel == 2):
    print("***Gasolina***")
    print("----------------")
    valCombustivel = 3.30
    if (litros <= 20):
        desconto = valCombustivel * 0.04
    else:
        desconto = valCombustivel * 0.06   
    
valFinal = (valCombustivel * litros) - desconto
print(f"Valor pago: R${valFinal}")

