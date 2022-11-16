names = input().split()
i = 0
sum = 0
while i < len(names[0]) and i < len(names[1]):
    sum += ord(names[0][i]) * ord(names[1][i])
    i += 1

while i < len(names[1]):
    sum += ord(names[1][i])
    i += 1

while i < len(names[0]):
    sum += ord(names[0][i])
    i += 1

print(sum)