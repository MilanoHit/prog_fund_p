team_A = []
team_B = []
for n in range(1, 12):
    team_A.append(n)
    team_B.append(n)
arr = input().split()
for p in range(0, len(arr)):
    if arr[p][0] == "A":
        arr[p] = arr[p].replace("A-", "")
        if int(arr[p]) in team_A:
            team_A.remove(int(arr[p]))
    if arr[p][0] == "B":
        arr[p] = arr[p].replace("B-", "")
        if int(arr[p]) in team_B:
            team_B.remove(int(arr[p]))
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")