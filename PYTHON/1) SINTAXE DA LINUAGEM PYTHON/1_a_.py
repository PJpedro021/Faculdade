# 1. Sintaxe da Linguagem Python
# a) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5%
# sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

salarioFixo = float(input('diite seu salario fixo: '))
print("Salario fixo: ",salarioFixo)
print("----------------------------")

valVendas = float(input('digite suas vendas: '))
print("Total de vendas: ",valVendas)
print("----------------------------")

print("Se total de vendas for menor que 1500 recebe 3% de comissão, se maior que 1500 recebe 3% + 5%")
print("----------------------------")

if(valVendas > 1500):
    a = valVendas * 0.05
    b = valVendas * 0.03
    print("Salario com comissão maior de 1500: ", salarioFixo + a + b)    

else:
     a = valVendas * 0.03
     print("Salario com comisão menor que 1500:", salarioFixo + a)
    
