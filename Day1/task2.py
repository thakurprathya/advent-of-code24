with open('./task2_input.txt', 'r') as f:
    input = f.read()

input = input.split('\n')

left, right = [], []
for row in input:
    row = row.split('   ')
    left.append(int(row[0]))
    right.append(int(row[1]))

left.sort()
right.sort()

cnt = {key: 0 for key in left}
for i in range(len(left)):
    if right[i] in cnt:
        cnt[right[i]] = cnt[right[i]] + 1 

res = 0
for i in range(len(left)):
    res += (left[i] * cnt[left[i]])
print(res)
