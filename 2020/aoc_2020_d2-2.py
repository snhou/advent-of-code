with open("aoc-2020-day2-1.txt", "r") as file:
    data = file.read()

data = data.split("\n")
datas = []
for each_record in data:
    datas.append(each_record.split(" "))
correct_count = 0
for i in datas:
    num_range = i[0].split("-")
    bottom, top = int(num_range[0]),int(num_range[1])
    subString = i[2][bottom-1]+i[2][top-1]
    if subString.count(i[1][0])==1:
        correct_count +=1
print("correct_count",correct_count)