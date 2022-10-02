from math import floor
n = int(input())
value = 0
top_weight = 0
top_time = 0
top_quality = 0
for k in range(0, n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    if (weight/time) ** quality > value:
        value = ((weight/time) ** quality)
        top_weight = weight
        top_time = time
        top_quality = quality
print(f"{top_weight} : {top_time} = {floor(value)} ({top_quality})")
