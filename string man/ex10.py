tickets = input().split(", ")

for i in range(0, len(tickets)):
    if len(tickets[i]) != 20:
        print("invalid ticket")
        continue
    if tickets[i].count("@") == 20 or tickets[i].count("^") == 20 or tickets[i].count("#") == 20 or tickets[i].count("$") == 20:
        print(f"ticket \"{tickets[i]}\" - 10{tickets[0][0]} Jackpot!")
        continue
    printed = False
    for p in range(0, 5):
        if tickets[i][p] == "@" or tickets[i][p] == "$" or tickets[i][p] == "#" or tickets[i][p] == "^":
            count = 1
            max1 = 0
            for j in range(p + 1, 10):
                if tickets[i][j] == tickets[i][p]:
                    count += 1
                    if count > max1:
                        max1 = count
                else:
                    break
            if max1 >= 6:
                for j in range(10, 15):
                    count2 = 0
                    max2 = 0
                    if tickets[i][j] == tickets[i][p]:
                        for k in range(j + 1, 20):
                            if tickets[i][j] == tickets[i][p]:
                                count2 += 1
                                if count2 > max2:
                                    max2 = count2
                            else:
                                break
                    if max1 == max2:
                        print(f"ticket \"{tickets[i]}\" - {count}{tickets[i][p]}")
                        printed = True
                        break
                if printed:
                    break
            if printed:
                break
    if printed:
        continue
    print(f"ticket \"{tickets[i]}\" - no match")
