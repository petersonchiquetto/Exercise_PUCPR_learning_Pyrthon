times = []
tabela = [0, 0, 0, 0]
 
for _ in range(4):
    time = input("Digite o nome de um dos times: ")
    times.append(time)
for i in range(3):
    for j in range(i+1,4):
        print("Jogo:", times[i], "x", times[j])
        gols1 = int(input("Gols do " + times[i] + ": "))
        gols2 = int(input("Gols do " + times[j] + ": "))
        if gols1 > gols2:
            tabela[i] += 3
        elif gols1 < gols2:
            tabela[j] += 3
        else:
            tabela[i] += 1
            tabela[j] += 1
print("*** Pontuação dos Times ***")
for i in range(4):
    print(times[i] + ": ", tabela[i])
maior = max(tabela)
print("****** Time Campeão ******")
for i in range(4):
    if tabela[i] == maior:
        print(times[i])