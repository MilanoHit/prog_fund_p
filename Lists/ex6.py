arr = input().split()
for k in range(0, len(arr)):
    arr[k] = int(arr[k])
n = int(input())
for p in range(0, n):
    small_num = 0
    for k in range(0, len(arr)):
        if k == 0:
            small_num = int(arr[k])
        elif int(arr[k]) < small_num:
            small_num = arr[k]
    arr.remove(small_num)
for k in range(0, len(arr)):
    if k != len(arr) -1:
        print(arr[k], end=", ")
    else:
        print(arr[k])
