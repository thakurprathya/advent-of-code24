with open('./task1_input.txt', 'r') as f:
    input = f.read()

input = input.split('\n')

left, right = [], []
for row in input:
    row = row.split('   ')
    left.append(int(row[0]))
    right.append(int(row[1]))

left.sort()
right.sort()

res = 0
for i in range(len(left)):
    res += abs(left[i] - right[i])

print(res)
