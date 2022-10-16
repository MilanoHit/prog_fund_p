arr = input().split()
for p in range(0, len(arr)):
    arr[p] = arr[p].replace(',', '')
n = int(input())
beggers = []
for p in range(0, n):
    beggers.append(0)
for p in range(0, len(arr)):
    beggers[p%n] += int(arr[p])
print(beggers)