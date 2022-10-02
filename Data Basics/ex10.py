lost_games = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
cost = 0
for k in range(1, lost_games + 1):
    if k % 2 == 0:
        cost += helmet
    if k % 3 == 0:
        cost += sword
    if k % 6 == 0:
        cost += shield
    if k % 12 == 0:
        cost += armor
print(f"Gladiator expenses: {cost:.2f} aureus")