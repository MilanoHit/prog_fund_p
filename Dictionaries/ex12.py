command = input().split('-')
students = {}
languages = []

while command[0] != "exam finished":
    if command[1] != "banned":
        if command[0] in students.keys():
            if command[1] == students[command[0]][0] and command[2] < students[command[0]][1]:
                languages[languages.index(command[1]) + 1] += 1
                command = input().split("-")
                continue
        if command[1] not in languages:
            languages.append(command[1])
            languages.append(1)
        else:
            languages[languages.index(command[1]) + 1] += 1
        language_score = [command[1], command[2]]
        students[command[0]] = language_score
    else:
        if command[0] in students.keys():
            students[command[0]][1] = "banned"
    command = input().split("-")

print("Results:")
for keys in students.keys():
    if students[keys][1] == "banned":
        continue
    print(f"{keys} | {students[keys][1]}")
print("Submissions:")
for i in range(0, len(languages), 2):
    print(f"{languages[i]} - {languages[i + 1]}")
