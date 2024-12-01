import os
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))
list1 = []
list2 = []
res1 = 0
res2 = 0
with open(dir_path + '\input.txt', 'r') as file:
    data = file.read().splitlines()
    for i in range(len(data)):
        splited = data[i].split('   ')
        list1.append(int(splited[0]))
        list2.append(int(splited[1]))

list1.sort()
list2.sort()
counts = Counter(list2)
for i in range(len(list1)):
    res1 = res1 + abs(list1[i] - list2[i])
    res2 = res2 + list1[i] * counts[list1[i]]

print(res1)
print(res2)