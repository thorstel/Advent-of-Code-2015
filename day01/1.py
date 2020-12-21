with open('input.txt', 'r') as f:
    data = f.read()

# Part 1
print(data.count('(') - data.count(')'))

# Part 2
num = 1
floor = 0

for c in data:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    else:
        assert False
    if floor == -1:
        break
    num += 1

print(num)
