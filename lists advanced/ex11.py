arr = input().split(", ")

command = input().split(":")

while command[0] != "course start":
    if command[0] == "Insert":
        if command[1] not in arr:
            arr.insert(int(command[2]), command[1])
    if command[0] == "Add":
        if command[1] not in arr:
            arr.append(command[1])
    if command[0] == "Remove":
        if command[1] in arr:
            if command[1] + "-Exercise" in arr:
                arr.remove(command[1] + "-Exercise")
            arr.remove(command[1])
    if command[0] == "Swap":
        if command[1] in arr and command[2] in arr:
            get = arr[arr.index(command[1])], arr[arr.index(command[2])]
            arr[arr.index(command[2])], arr[arr.index(command[1])] = get
            if command[1] + "-Exercise" in arr:
                arr.remove(command[1] + "-Exercise")
                arr.insert(int(arr.index(command[1])) + 1, command[1] + "-Exercise")
            if command[2] + "-Exercise" in arr:
                arr.remove(command[2] + "-Exercise")
                arr.insert(int(arr.index(command[2])) + 1, command[2] + "-Exercise")
    if command[0] == "Exercise":
        if command[1] not in arr:
            arr.append(command[1])
            arr.append(command[1] + "-Exercise")
        else:
            arr.insert(arr.index(command[1]) + 1, command[1] + "-Exercise")
    command = input().split(":")

for n in range(0, len(arr)):
    print(f"{n + 1}.{arr[n]}")