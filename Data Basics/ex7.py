n = int(input())
sum = 0
for k in range(0, n):
    c = int(input())
    if c > 255 - sum:
        print("Insufficient capacity!")
        continue
    else:
        sum += c
print(sum)