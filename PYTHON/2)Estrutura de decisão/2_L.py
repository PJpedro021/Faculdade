# l) Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo na linguagem
# Python que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
print("Digite sua idade para saber se pode doar sangue")
idade = float(input("idade: "))

if( idade < 18):
    print("Não pode doar")    
elif(idade > 67):
    print("Não pode doar")    
else:
    print("Pode doar!")