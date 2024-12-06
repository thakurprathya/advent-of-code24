with open('./task1_input.txt', 'r') as f:
    input = f.read()

input = input.split('\n')

res = 0
for report in input:
    levels = report.split(' ')
    increasing = all(int(levels[i]) > int(levels[i-1]) for i in range(1, len(levels)))
    decreasing = all(int(levels[i]) < int(levels[i-1]) for i in range(1, len(levels)))

    if not (increasing or decreasing):
        continue
    
    check = True
    for i in range(1, len(levels)):
        if abs(int(levels[i]) - int(levels[i-1])) < 1 or abs(int(levels[i]) - int(levels[i-1])) > 3:
            check = False
            break
        
    if not check: continue
    res += 1

print(res)