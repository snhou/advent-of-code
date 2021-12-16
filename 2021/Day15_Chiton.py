with open("Day15_Chiton.txt") as file:
    data = file.read()

raw = []
for i in data.split("\n"):
    raw.append([int(j) for j in list(i)])

# for t in raw:
#     print(t)
# exit()

risk_total = raw[0][0]
for l in range(len(raw)):
    for w in range(len(raw[0])):
        try:
            right = risk_total + raw[l][w+1]
            down = risk_total + raw[l+1][w]
            if right >= down:
                raw = [row[1:] for row in raw]
                risk_total = right
            elif right < down:
                raw = raw[1:]
                risk_total = down
            else:
                pass
        except:
            print(risk_total)
