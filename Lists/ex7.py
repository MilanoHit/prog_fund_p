gifts = input().split()
command = input().split()
while command[0] != 'No':
    if command[0] == "OutOfStock":
        for p in range(0, len(gifts) - 1):
            if gifts[p] == command[1]:
                gifts[p] = None
    if command[0] == "Required":
        if int(command[2]) < len(gifts):
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    if command[0] == "JustInCase":
        gifts[len(gifts) - 1] = command[1]
    command = input().split()
for n in range(0, len(gifts)):
    if gifts[n] != None:
        print(gifts[n], end=' ')