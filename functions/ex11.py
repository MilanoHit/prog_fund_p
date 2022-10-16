list = []
for n in range(0, 10):
    list.append('.')
n = int(int(input())/10)
for p in range(0, n):
    list[p] = "%"
if n != 10:
    print(f"{n*10}%", end= " ")
    print("[", end="")
    for z in range(0, 10):
        print(list[z], end="")
    print("]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")