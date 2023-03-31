# e) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se
# saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever
# a mensagem 'Saldo Negativo'.


saldo = float(input("Digite seu saldo: "))
print("---------------------")
debito = float(input("Digite seu debito: "))
print("---------------------")
credito = float(input("Digite seu credito: "))
print("---------------------")

print("Saldo: ",saldo," Debito ", debito," Crédito:")
print("---------------------")

if(saldo <= 0):
    print("Saldo negativo")
else:
    print("Saldo positivo")
    
    
