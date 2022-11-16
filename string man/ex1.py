names = input().split(", ")
namesreworked = []
for i in range(0, len(names)):
    viable = True
    if len(names[i]) > 16 or len(names[i]) < 3:
        continue
    for p in range(0, len(names[i])):
        if "a" <= names[i][p] <= "z" or "A" <= names[i][p] <= "Z" or names[i][p] == "-" or names[i][p] == "_" or "0" <= names[i][p] <= "9":
            continue
        else:
            viable = False
            break
    if viable:
        namesreworked.append(names[i])
for i in namesreworked:
    print(i)