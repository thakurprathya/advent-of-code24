def solve(levels):
    increasing = all(int(levels[i]) > int(levels[i-1]) for i in range(1, len(levels)))
    decreasing = all(int(levels[i]) < int(levels[i-1]) for i in range(1, len(levels)))

    if not (increasing or decreasing):
        return False
    
    for i in range(1, len(levels)):
        if abs(int(levels[i]) - int(levels[i-1])) < 1 or abs(int(levels[i]) - int(levels[i-1])) > 3:
            return False
    return True


with open('./task2_input.txt', 'r') as f:
    input = f.read()

input = input.split('\n')
lists = []
for report in input:
    nums = report.split(' ')
    for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        lists.append(temp)

res = 0
i = 0
for report in input:
    report = report.split(' ')
    for j in range(len(report)):
        if(solve(lists[i+j])):
            res += 1
            break
    i += len(report)

print(res)