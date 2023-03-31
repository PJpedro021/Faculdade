# t) Faça um script em Python que calcule o fatorial de um número 𝑛 informado pelo usuário.
# O fatorial de um número é calculado pela multiplicação desse número por todos os seus
# antecessores até chegar ao número 1. 
print("Calculo de Fatorial")
print("-----------")
n = int(input("Digite um número: "))
print("-----------")
x = 1
for i in range(1, n+1):
    x = x * i
print(f"O fatorial de {n} é {x}")
