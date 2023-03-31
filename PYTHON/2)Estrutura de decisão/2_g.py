# g) Programa em Python que leia o nome de 2 times e o número de gols marcados na partida
# (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser
# impressa a palavra EMPATE. 
print ("*****Digite o numero de gols*****")

time1 = int(input("Time 1: "))
time2 = int(input("Time 2: "))

print("*********************************")

if(time1 > time2):
    print("Time 1 venceu!!!")
    print(f"Gols:{time1} ")
    
elif(time2 > time1):
    print("Time 2 venceu!!")
    print(f"Gols: {time2}")
else:
    print(f"Jogo empatado!!")
    print(f'Gols time 1: {time1}')
    print(f'Gols time 2: {time2}')
    
    