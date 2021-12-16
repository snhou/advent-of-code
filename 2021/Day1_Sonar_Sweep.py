with open("Day1_Sonar_Sweep.txt") as file:
    data = file.read()

raw = []
for i in data.split("\n"):
    raw.append(int(i))

measurement = []
for j in raw:
    if j == 1:
        measurement.append("")