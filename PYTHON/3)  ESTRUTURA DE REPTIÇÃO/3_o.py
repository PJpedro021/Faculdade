# o) Crie um algoritmo em Python que, dado um número informado pelo usuário, imprima a
# tabuada dele de 1 a 10. Use o formato de apresentação.

num = int(input("Digite um numero: "))
print(f"Tabuada de {num}")

for i in range(11):
     print(i * num)
