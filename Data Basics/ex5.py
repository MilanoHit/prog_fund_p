n = int(input())
for k in range(ord("a"), ord("a") + n):
    for p in range(ord("a"), ord("a") + n):
        for d in range(ord("a"), ord("a") + n):
            print(chr(k) + chr(p) + chr(d))