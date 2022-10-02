from math import floor
group_size = int(input())
days = int(input())
total_coins = 0
for n in range(1, days + 1):
    total_coins += 50
    if n % 10 == 0:
        group_size -= 2
    if n % 15 == 0:
        group_size += 5
    total_coins -= 2*group_size
    if n % 3 == 0:
        total_coins -= group_size * 3
    if n % 5 == 0:
        total_coins += group_size*20
    if n % 15 == 0:
        total_coins -= group_size * 2
print(f"{group_size} companions received {floor(total_coins / group_size)} coins each.")