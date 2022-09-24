quantity = int(input())
days = int(input())
spirit = 0
budget = 0
k = 0

for n in range(days, 0, -1):
    k += 1
    if k % 11 == 0:
        quantity += 2
    if k % 2 == 0:
        budget += 2 * quantity
        spirit += 5
    if k % 3 == 0:
        budget += 8 * quantity
        spirit += 13
    if k % 5 == 0:
        budget += 15 * quantity
        spirit += 17
    if k % 15 == 0:
        spirit += 30
    if k % 10 == 0:
        spirit -= 20
        budget += 23
    if n == 1 and k % 10 == 0:
        spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")