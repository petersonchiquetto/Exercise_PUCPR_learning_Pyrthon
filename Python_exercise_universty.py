nums = []
maiores = []
menores = []
soma = 0
for _ in range(6):
    num = int(input("Informe um dos 6 números: "))
    nums.append(num)
    soma += num
media = soma / 6
for num in nums:
    if num >= media:
        maiores.append(num)
    else:
        menores.append(num)
print("A média dos 6 números é", media)
print("Os números iguais ou maiores que a média são", maiores)
print("Os números menores que a média são", menores)