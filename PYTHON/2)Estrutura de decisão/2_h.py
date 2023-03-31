# h) Escreva um programa em Python que recebe um inteiro e informe se é par ou ímpar.
# divisão dele por 2. Se o resultado for 0

print("Digite algum numero para saber se é par ou impar")
num = int(input("numero: "))

if(num %2 == 0):
    print("Numero é par")
else:
    print("Numero é impar")