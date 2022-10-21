arr = input().split()
for i in  range(0, len(arr)):
    arr[i] = int(arr[i])
command = input()

while command != "End":
    if int(command) > len(arr) - 1:
        command = input()
        continue
    if arr[int(command)] == -1:
        command = input()
        continue
    for n in range (0, len(arr)):
        if arr[int(command)] < arr[n]:
            arr[n] -= arr[int(command)]
        else:
            if int(command) != n and arr[n] != -1:
                arr[n] += arr[int(command)]
    arr[int(command)] = -1
    command = input()

counter = 0
for i in range (0, len(arr)):
    if arr[i] == -1:
        counter += 1

print(f"Shot targets: {counter} ->", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")