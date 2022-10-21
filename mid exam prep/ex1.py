food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
checker = 0
for n in range(1, 31):
    food -= 0.3
    if n % 2 == 0:
        hay -= food*5/100
    if n % 3 == 0:
        cover -= weight/3
    if food < 0 or hay < 0 or cover < 0:
        print("Merry must go to the pet store!")
        checker = 1
        break

if checker == 0:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")