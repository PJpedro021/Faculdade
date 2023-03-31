# j) Ler as notas da 1ª , 2ª e 3ª avaliações de um aluno. Calcular a média aritmética simples e
# escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota
# igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada

av1 = float(input("Nota 1: "))
av2 = float(input("Nota 2: "))
av3 = float(input("Nota 3: "))

media = (av1 + av2 + av3) / 3

if(media < 6):
    print(f"Aluno Reprovado, {media} :(")
else:
    print(f"Aluno Aprovado!!, {media} :)")