b = [35, 453, 537, 777, 790, 810, 863, 983, 1037, 1038, 1051, 1067, 1139, 1174, 1222]
import random
for i in range(100):
    a = random.sample(b,3)
    if sum(a)==2020:
        print(a)